import argparse
import envs
import deciders
from matplotlib import animation
import matplotlib.pyplot as plt
import os
import numpy as np
import torch as th
from envs.translator import InitSummarizer, CurrSummarizer, FutureSummarizer, Translator
from tianshou.data import Collector, VectorReplayBuffer, ReplayBuffer
from tianshou.policy import PPOPolicy
from RL_based.utils import (
    Net_GRU_Bert_tianshou,
    Net_Bert_CLS_tianshou,
    Net_Bert_CNN_tianshou,
    Net_GRU_nn_emb_tianshou,
)
from tianshou.utils.net.common import ActorCritic
from tianshou.utils.net.discrete import Actor, Critic
import gym
import json

ENV_CLASS = {'classic_control': ['CartPole', 'Acrobot', 'MountainCar'],
             'box2d': ['LunarLander'],
             'toy_text': ['Blackjack', 'Taxi', 'CliffWalking', 'FrozenLake']}

def get_env_class(env_name):
    for key, value in ENV_CLASS.items():
        if env_name in value:
            return key
    return None

def get_fewshot_example_path(env, decider):
    assert decider in ['random_actor', 'expert'], "decider must be random_actor or expert"
    prompt_level = 2 if decider == 'random_actor' else 4
    fewshot_example_path = os.path.join(
        'envs', get_env_class(env.spec.name), 'few_shot_examples',
        ''.join([env.spec.name.lower(), '_l', str(prompt_level), '.json']))
    return fewshot_example_path

# https://colab.research.google.com/drive/1DdWsGi10232orUv-reY4wsTmT0VMoHaX?usp=sharing#scrollTo=4OfVmDKk7XvG
# LLMs bias on 0 so make the actions greater than 1 instead.

def gen_expert_examples(environment, policy, file_path, max_episode_len=120, n_episodes=1):
    replaybuffer = ReplayBuffer(size=1000)
    test_collector_1 = Collector(policy, environment, replaybuffer)
    test_collector_1.reset_env()
    game_description = environment.get_game_description()
    goal_description = environment.get_goal_description()
    action_description = environment.get_action_description()
    policy.eval()
    data_lst = []

    for _ in range(n_episodes):
        test_collector_1.reset_buffer()
        result = test_collector_1.collect(n_episode=1)
        sample_result = replaybuffer.sample(0)[0]
        round = 0 
        utility = 0
        data = []
        for transition in sample_result:
            round += 1
            if round > max_episode_len:
                break
            question = f"{transition.obs} \n {goal_description} \n {action_description} "
            reward = transition.rew
            utility += reward

            answer = f"The final answer is: {transition.act + 1}"

            data.append(
                {   
                    "observation": transition.obs, 
                    "goal_description": goal_description, 
                    "action_description": action_description, 
                    "game_description": game_description,
                    "action": str(transition.act + 1),
                    "question": question,
                    "answer": answer,
                    "reward": reward,
                    "cum_reward": utility,
                }
            )
            print(f"Now it is round {round}")
        data_lst.append(data)
    # Return the final reward
    with open(file_path, "w") as outfile:
        json.dump(data_lst, outfile)
    return utility


def gen_examples(environment, decider, file_path, max_episode_len=200, n_episodes=1):
    game_description = environment.get_game_description()
    goal_description = environment.get_goal_description()
    action_description = environment.get_action_description()
    frames = []
    utilities = []
    data_lst = []

    for _ in range(n_episodes):
        # Reset the environment
        round = 0
        state_description, env_info = environment.reset()
        utility = 0
        data = []
        for _ in range(max_episode_len):
            # Keep asking ChatGPT for an action until it provides a valid one  
            asking_round = 0
            action, prompt, answer, _, _, _ = decider.act(
                state_description,
                action_description,
                env_info,
                game_description,
                goal_description,
            )
            # Perform the action in the environment
            state_description, reward, terminated, truncated, env_info = environment.step_llm(
                action
            )
            question = f"{state_description} \n {goal_description} \n {action_description} "
            utility += reward
            answer += f"The final answer is: {action}"

            data.append(
                {
                    "observation": state_description, 
                    "goal_description": goal_description, 
                    "action_description": action_description, 
                    "game_description": game_description,
                    "action": action,
                    "question": question,
                    "answer": answer,
                    "reward": reward,
                    "cum_reward": utility,
                }
            )
            print(f"Now it is round {round}")
            round += 1
            # If the game is over, break the loop
            if terminated or truncated:
                print(f"Terminated!")
                break
        utilities.append(utility)
        data_lst.append(data)
    # Return the final reward
    with open(file_path, "w") as outfile:
        json.dump(data_lst, outfile)
    return utility


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate few shots examples of a gym environment."
    )
    parser.add_argument(
        "--init_summarizer",
        type=str,
        required=True,
        help="The name of the init summarizer to use.",
    )
    parser.add_argument(
        "--curr_summarizer",
        type=str,
        required=True,
        help="The name of the curr summarizer to use.",
    )
    parser.add_argument(
        "--env",
        type=str,
        default="base_env",
        help="The name of the gym environment to use.",
    )
    parser.add_argument(
        "--decider",
        type=str,
        default="naive_actor",
        help="The actor used to select action",
    )
    parser.add_argument(
        "--env_name",
        type=str,
        default="CartPole-v0",
        help="The name of the gym environment to use.",
    )
    parser.add_argument(
        "--max_episode_len",
        type=int,
        default=200,
        help="The maximum number of steps in an episode.",
    )
    parser.add_argument(
        "--num_episodes",
        type=int,
        default=1,
        help="The number of episodes to collect data.",
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=128,
        help="The token length of the observation",
    )
    parser.add_argument(
        "--trans_model_name",
        type=str,
        default="/home/ubuntu/LLM-Decider-Bench/RL_based/transformer_offline_distilbert",
        help="The name of the pretrained transformer to use.",
    )
    parser.add_argument(
        "--policy_path",
        type=str,
        default=None,
        help="The path to the policy to be evaluated",
    )
    parser.add_argument(
        "--n_episodes",
        type=int,
        default=2,
        help="The number of episodes to collect data (for env where episode is too short).",
    )

    args = parser.parse_args()
    # Get the specified translator, environment, and ChatGPT model
    device = "cuda" if th.cuda.is_available() else "cpu"
    env_class = envs.REGISTRY[args.env]
    init_summarizer = InitSummarizer(envs.REGISTRY[args.init_summarizer])
    curr_summarizer = CurrSummarizer(envs.REGISTRY[args.curr_summarizer])
    translator = Translator(init_summarizer, curr_summarizer, None, env=None)
    environment = env_class(gym.make(args.env_name, render_mode=None), translator)

    fewshot_example_path = get_fewshot_example_path(environment, args.decider)

    if args.decider == "expert":
        net = Net_GRU_nn_emb_tianshou(
            hidden_sizes=[256, 128],
            device=device,
            max_length=args.max_length,
            trans_model_name=args.trans_model_name,
        )
        actor = Actor(net, environment.action_space.n, device=device).to(device)
        critic = Critic(net, device=device).to(device)
        actor_critic = ActorCritic(actor, critic)
        optim = th.optim.Adam(actor_critic.parameters(), lr=0.0003)

        # PPO policy
        dist = th.distributions.Categorical
        policy = PPOPolicy(
            actor,
            critic,
            optim,
            dist,
            action_space=environment.action_space,
            deterministic_eval=True,
        )
        policy.load_state_dict(th.load(args.policy_path))
        utility = gen_expert_examples(
            environment, policy, fewshot_example_path,
            max_episode_len=args.max_episode_len, n_episodes=args.n_episodes
        )
    else:
        decider_class = deciders.REGISTRY[args.decider]
        decider = decider_class(environment.env.action_space)
        # Evaluate the translator
        utility = gen_examples(
            environment, decider, fewshot_example_path,
            max_episode_len=args.max_episode_len, 
            n_episodes=args.n_episodes
        )
    print(f"(Avg.) Cummulative reward: {utility}")
