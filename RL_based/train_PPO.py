import argparse
import sys
sys.path.insert(0, sys.path[0]+"/../")
import prompts as task_prompts
import envs
import os
from envs.translator import InitSummarizer, CurrSummarizer, FutureSummarizer, Translator
import gym
from torch.optim.lr_scheduler import LambdaLR
import torch
from tianshou.data import Collector, VectorReplayBuffer, ReplayBuffer
from tianshou.env import DummyVectorEnv, SubprocVectorEnv
from tianshou.policy import PPOPolicy, ICMPolicy
from tianshou.trainer import onpolicy_trainer
from tianshou.utils.net.common import ActorCritic
from tianshou.utils.net.discrete import Actor, Critic, IntrinsicCuriosityModule
from RL_based.utils import Net_GRU_Bert_tianshou, Net_Bert_CLS_tianshou, Net_Bert_CNN_tianshou, Net_GRU_nn_emb_tianshou
from tianshou.utils import WandbLogger
from torch.utils.tensorboard import SummaryWriter
from tianshou.trainer.utils import test_episode

import warnings
warnings.filterwarnings('ignore')

class MaxStepLimitWrapper(gym.Wrapper):
    def __init__(self, env, max_steps=200):
        super(MaxStepLimitWrapper, self).__init__(env)
        self.max_steps = max_steps
        self.current_step = 0

    def reset(self, **kwargs):
        self.current_step = 0
        return self.env.reset(**kwargs)

    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)
        self.current_step += 1

        if self.current_step >= self.max_steps:
            terminated = True
            info['episode_step_limit'] = self.max_steps

        return observation, reward, terminated, truncated, info

class SimpleTextWrapper(gym.Wrapper):
    def __init__(self, env):
        super(SimpleTextWrapper, self).__init__(env)
        self.env = env

    def reset(self, **kwargs):
        observation, _ = self.env.reset(**kwargs)
        return str(observation), {}

    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)
        return str(observation), reward, terminated, truncated, info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate a translator in a gym environment with a ChatGPT model.')
    parser.add_argument('--init_summarizer', type=str, required=True, help='The name of the init summarizer to use.')
    parser.add_argument('--curr_summarizer', type=str, required=True, help='The name of the curr summarizer to use.')
    parser.add_argument('--future_summarizer', type=str, help='The name of the future summarizer to use.')
    parser.add_argument('--env', type=str, default='base_env', help='The name of the gym environment to use.')
    parser.add_argument('--env_name', type=str, default='CartPole-v1', help='The name of the gym environment to use.')
    parser.add_argument('--decider', type=str, default="naive_actor", help='The actor used to select action')
    parser.add_argument('--render', type=str, default="rgb_array", help='The render mode')
    parser.add_argument('--future_horizon', type=int, help='The horizon of looking to future')
    parser.add_argument(
        "--prompt_level",
        type=int,
        default=1,
        help="The level of prompts",
    )
    parser.add_argument(
        "--past_horizon", type=int, help="The horizon of looking back"
    )
    parser.add_argument(
        "--max_episode_len", type=int, default=200, help="The max length of an episode"
    )

### for RL training
    parser.add_argument('--max_length', type=int, default=128, help='The token length of the observation')
    # trans_model_name
    parser.add_argument('--trans_model_name', type=str, default='bert-base-uncased', help='The name of the pretrained transformer to use.')
    parser.add_argument('--model_name', type=str, default='bert-embedding', help='The name of the model to use.')
    parser.add_argument('--vector_env', type=str, default='dummy', help='The name of the vector env to use.')
    parser.add_argument('--eval', action='store_true', default=False, help='Whether to only eval the model')
    parser.add_argument('--policy-path', type=str, default=None, help='The path to the policy to be evaluated')
    parser.add_argument('--collect_one_episode', action='store_true', default=False, help='Whether to only collect one episode')
    parser.add_argument('--lr', type=float, default=0.0003, help='The learning rate of the model')
    parser.add_argument('--step_per_epoch', type=int, default=10000, help='The number of steps per epoch')
    parser.add_argument('--step_per_collect', type=int, default=2000, help='The number of steps per collect')
    parser.add_argument('--lr_decay', action='store_true', default=False, help='Whether to decay the learning rate')
    parser.add_argument('--epoch', type=int, default=400, help='The number of epochs to train')
    parser.add_argument('--resume_path', type=str, default=None, help='The path to the policy to be resumed')
    parser.add_argument('--taxi_specific_env', action='store_true', default=False, help='Whether to use taxi specific env')
    parser.add_argument(
        "--frameskip",
        type=int,
        default=4,
        help="The frameskip for atari environments",
    )
    args = parser.parse_args()
    args_dict = vars(args)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # Get the specified translator, environment, and ChatGPT model
    env_class = envs.REGISTRY[args.env]
    init_summarizer = InitSummarizer(envs.REGISTRY[args.init_summarizer])
    curr_summarizer = CurrSummarizer(envs.REGISTRY[args.curr_summarizer])
    if args.future_summarizer:
        future_summarizer = FutureSummarizer(
            envs.REGISTRY[args.future_summarizer],
            envs.REGISTRY["cart_policies"],
            future_horizon=args.future_horizon,
        )
    else:
        future_summarizer = None

    wandb_log_config = {
        "env": args.env_name,
        "init_summarizer": args.init_summarizer,
        "curr_summarizer": args.curr_summarizer,
        "future_summarizer": args.future_summarizer,
    }
    wandb_log_config.update(args_dict)

    if not args.eval:
        logger = WandbLogger(
            project="LLM-decider-bench-RL",
            entity="llm-bench-team",
            config=wandb_log_config,
        )
        random_name = logger.wandb_run.name
        log_path = os.path.join('./RL_based/results', args.env_name, random_name)
        writer = SummaryWriter(log_dir=log_path)
        writer.add_text("args", str(args))
        logger.load(writer)
        def save_best_fn(policy):
            torch.save(policy.state_dict(), os.path.join(log_path, 'policy.pth'))

    sampling_env = envs.REGISTRY["sampling_wrapper"](gym.make(args.env_name))
    if args.prompt_level == 5:
        prompts_class = task_prompts.REGISTRY[(args.env_name,args.decider)]()
    else:
        prompts_class = task_prompts.REGISTRY[(args.decider)]()
    translator = Translator(
        init_summarizer, curr_summarizer, future_summarizer, env=sampling_env
    )
    if 'Represented' in args.env_name:
        environment = env_class(
            gym.make(args.env_name, render_mode=args.render, frameskip=args.frameskip), translator
        )
    else:
        environment = env_class(
            gym.make(args.env_name, render_mode=args.render), translator
        )
    
    # Set the translation level
    translate_level = 1
    if args.past_horizon is None and args.future_horizon is None:
        translate_level = 1
    if args.past_horizon and args.future_horizon is None:
        raise NotImplementedError
        # translate_level = 2
    if args.past_horizon is None and args.future_horizon:
        raise NotImplementedError
        # translate_level = 3
    if args.past_horizon and args.future_horizon:
        raise NotImplementedError
        # translate_level = 3.5


    if args.vector_env == 'dummy':
        ThisEnv = DummyVectorEnv
    elif args.vector_env == 'subproc':
        ThisEnv = SubprocVectorEnv
    def make_env():
        if args.taxi_specific_env:
            env = MaxStepLimitWrapper(SimpleTextWrapper(gym.make(args.env_name, render_mode=args.render)), max_steps=200)
            env._max_episode_steps = args.max_episode_len
        else:
            env = env_class(MaxStepLimitWrapper(gym.make(args.env_name, render_mode=args.render), max_steps=200), translator)
            env._max_episode_steps = args.max_episode_len
        
        return env
    train_envs = ThisEnv([make_env for _ in range(20)])
    test_envs = ThisEnv([make_env for _ in range(10)])
    # model & optimizer
    def get_net():
        if args.model_name == "bert-embedding":
            net = Net_GRU_Bert_tianshou(state_shape=environment.observation_space.shape, hidden_sizes=[64, 64], device=device, max_length=args.max_length, trans_model_name=args.trans_model_name)    
        elif args.model_name == "bert-CLS-embedding":
            net = Net_Bert_CLS_tianshou(state_shape=environment.observation_space.shape, hidden_sizes=[256, 128], device=device, max_length=args.max_length, trans_model_name=args.trans_model_name)
        elif args.model_name == "bert-CNN-embedding":
            net = Net_Bert_CNN_tianshou(state_shape=environment.observation_space.shape, hidden_sizes=[256, 128], device=device, max_length=args.max_length, trans_model_name=args.trans_model_name)
        elif args.model_name == "nn_embedding":
            net = Net_GRU_nn_emb_tianshou(hidden_sizes=[256, 128], device=device, max_length=args.max_length, trans_model_name=args.trans_model_name)
        return net
    net = get_net()
    actor = Actor(net, environment.action_space.n, device=device).to(device)
    critic = Critic(net, device=device).to(device)
    actor_critic = ActorCritic(actor, critic)
    optim = torch.optim.Adam(actor_critic.parameters(), lr=args.lr)

    # PPO policy
    dist = torch.distributions.Categorical
    lr_scheduler = None
    if args.lr_decay:
            max_update_num = args.step_per_epoch // args.step_per_collect * args.epoch

            lr_scheduler = LambdaLR(optim, lr_lambda=lambda epoch: 1 - epoch / max_update_num)
    policy = PPOPolicy(actor, critic, optim, dist, action_space=environment.action_space, lr_scheduler=lr_scheduler).to(device)
    # collector
    train_collector = Collector(policy, train_envs, VectorReplayBuffer(20000, len(train_envs)), exploration_noise=True)
    test_collector = Collector(policy, test_envs, exploration_noise=True)

    if not args.eval:
        # trainer
        # test train_collector and start filling replay buffer

        if args.resume_path:
            policy.load_state_dict(torch.load(args.resume_path, map_location='cuda'))
            print("Loaded agent from: ", args.resume_path)

        train_collector.collect(256 * 20)
        result = onpolicy_trainer(
            policy,
            train_collector,
            test_collector,
            max_epoch=args.epoch,
            step_per_epoch=50000, # the number of transitions collected per epoch
            repeat_per_collect=4,
            episode_per_test=10,
            batch_size=256,
            logger=logger,
            step_per_collect=1000,  # the number of transitions the collector would collect before the network update
            save_best_fn=save_best_fn,
            # stop_fn=lambda mean_reward: mean_reward >= environment.spec.reward_threshold,
        )
        print(result)
    else:
        assert args.policy_path is not None
        policy.load_state_dict(torch.load(args.policy_path))
        test_collector = Collector(policy, test_envs)
        result = test_episode(policy, test_collector, None, None, n_episode=10)
        print(result)
        if args.collect_one_episode:
            replaybuffer = ReplayBuffer(size=1000)
            test_collector_1 = Collector(policy, environment, replaybuffer)
            test_collector_1.reset_env()
            test_collector_1.reset_buffer()
            policy.eval()
            result = test_collector_1.collect(n_episode=1)
            print('sample results', f"./RL_based/checkpoints/{args.env_name}/output.txt")
            sample_result = replaybuffer.sample(0)
            f = open(f"./RL_based/checkpoints/{args.env_name}/output.txt", "w")
            print(sample_result, file=f)
            f.close()