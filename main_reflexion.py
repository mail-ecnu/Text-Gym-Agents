import argparse
import envs
import deciders
import distillers
from matplotlib import animation
import matplotlib.pyplot as plt
import prompts as task_prompts
import os
import datetime
import time
from collections import deque
from envs.translator import InitSummarizer, CurrSummarizer, FutureSummarizer, Translator
import gym
import json
import pandas as pd
import random
import numpy as np
import datetime
from loguru import logger
from gym.spaces import Discrete




def set_seed(seed):
    random.seed(seed)

def save_frames_as_gif(frames, path="./", filename="gym_animation.gif"):
    # Mess with this to change frame size
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi=72)

    patch = plt.imshow(frames[0])
    plt.axis("off")

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval=50)

    # Ensure the folder exists, if it does not exist, create it
    os.makedirs(path, exist_ok=True)
    print(f"file name: {filename}")
    print(f"path name: {path}")
    anim.save(path + filename, writer="imagemagick", fps=60)


def evaluate_translator(translator, environment, decider, max_episode_len, logfile, args):
    utilities = []
    df = pd.read_csv('record_reflexion.csv', sep=',')
    filtered_df = df[(df['env'] == args.env_name) & (df['decider'] == 'expert') & (df['level'] == 1)]
    expert_score = filtered_df['avg_score'].item()
    seeds = [i for i in range(1000)]
    # prompt_file = "prompt.txt"
    # f = open(prompt_file,"w+")
    num_trails = args.num_trails
    if not "Blackjack" in args.env_name:
        curriculums = 1
    else:
        curriculums = 20
    for curriculum in range(curriculums):
        for trail in range(num_trails): 
            if "Blackjack" in args.env_name:
                seed = seeds[curriculum*curriculums + num_trails - trail - 1]
            else:
                seed = args.seed
            utility = _run(translator, environment, decider, max_episode_len, logfile, args, trail, seed) 
            utilities.append(utility)
            # TODO: set env sucess utility threshold
            if trail < num_trails -1:
                if args.decider in ['reflexion']:
                    if utility < expert_score: 
                        decider.update_mem() 
                else:
                    decider.update_mem() 
        decider.clear_mem()
    return utilities            

def _run(translator, environment, decider, max_episode_len, logfile, args, trail, seed):
    # Reset the environment
    if not "Blackjack" in args.env_name:
        set_seed(args.seed)
        seed = args.seed
        # Reset the environment
        state_description, env_info = environment.reset(seed=args.seed)
    else:
        set_seed(seed)
        # Reset the environment
        state_description, env_info = environment.reset(seed=seed)
    game_description = environment.get_game_description()
    goal_description = environment.get_goal_description()
    action_description = environment.get_action_description()

    # Initialize the statistics
    frames = []
    utility = 0
    current_total_tokens = 0
    current_total_cost = 0
    start_time = datetime.datetime.now()
    # Run the game for a maximum number of steps
    for round in range(max_episode_len):
        # Keep asking ChatGPT for an action until it provides a valid one
        error_flag = True
        retry_num = 1
        for error_i in range(retry_num):
            try:
                action, prompt, response, tokens, cost = decider.act(
                    state_description,
                    action_description,
                    env_info,
                    game_description,
                    goal_description,
                    logfile
                )

                state_description, reward, termination, truncation, env_info = environment.step_llm(
                    action
                )
                if "Cliff" in args.env_name or "Frozen" in args.env_name:
                    decider.env_history.add('reward', env_info['potential_state'] + environment.reward_desc_dict[reward])
                else:
                    decider.env_history.add('reward', f"The player get rewards {reward}.")
                    
                utility += reward

                # Update the statistics
                current_total_tokens += tokens
                current_total_cost += cost
                error_flag = False
                break
            except Exception as e:
                print(e)
                if error_i < retry_num-1:
                    if "Cliff" in args.env_name or "Frozen" in args.env_name:
                        decider.env_history.remove_invalid_state()
                    decider.env_history.remove_invalid_state()
                if logger:
                    logger.debug(f"Error: {e}, Retry! ({error_i+1}/{retry_num})")
                continue
        if error_flag:
            action = decider.default_action
            state_description, reward, termination, truncation, env_info = environment.step_llm(
                    action
                )

            decider.env_history.add('action', decider.default_action)

            if "Cliff" in args.env_name or "Frozen" in args.env_name:
                # decider.env_history.add('reward', reward)
                decider.env_history.add('reward', env_info['potential_state'] + environment.reward_desc_dict[reward])
            utility += reward

            
            logger.info(f"Seed: {seed}")
            logger.info(f'The optimal action is: {decider.default_action}.')
            logger.info(f"Now it is round {round}.")
        else:
            current_total_tokens += tokens
            current_total_cost += cost
            logger.info(f"Seed: {seed}")
            logger.info(f"current_total_tokens: {current_total_tokens}")
            logger.info(f"current_total_cost: {current_total_cost}")
            logger.info(f"Now it is round {round}.")

        # frames.append(environment.render())
        if termination or truncation:
            if logger:
                logger.info(f"Terminated!")
            break
        time.sleep(1)
    decider.env_history.add('terminate_state', environment.get_terminate_state(round+1, max_episode_len))
    decider.env_history.add("cummulative_reward", str(utility))
    # Record the final reward
    if logger:
        logger.info(f"Cummulative reward: {utility}.")
        end_time = datetime.datetime.now()
        time_diff = end_time - start_time
        logger.info(f"Time consumer: {time_diff.total_seconds()} s")
    return utility


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate a translator in a gym environment with a ChatGPT model."
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
        "--future_summarizer",
        type=str,
        help="The name of the future summarizer to use.",
    )
    parser.add_argument(
        "--env",
        type=str,
        default="base_env",
        help="The name of the gym environment to use.",
    )
    parser.add_argument(
        "--env_name",
        type=str,
        default="CartPole-v0",
        help="The name of the gym environment to use.",
    )
    parser.add_argument(
        "--decider",
        type=str,
        default="spp_actor",
        help="The actor used to select action",
    )
    parser.add_argument(
        "--gpt_version", type=str, default="gpt-3.5-turbo", help="The version of GPT to use"
    )
    parser.add_argument(
        "--render", type=str, default="rgb_array", help="The render mode"
    )
    parser.add_argument(
        "--max_episode_len",
        type=int,
        default=200,
        help="The maximum number of steps in an episode",
    )
    parser.add_argument(
        "--max_query_tokens",
        type=int,
        default=5000,
        help="The maximum number of tokens when querying",
    )
    parser.add_argument(
        "--max_generate_tokens",
        type=int,
        default=2000,
        help="The maximum number of tokens when responding",
    )
    parser.add_argument(
        "--frameskip",
        type=int,
        default=4,
        help="The frameskip for atari environments",
    )

    parser.add_argument(
        "--distiller",
        type=str,
        default="traj_distiller",
        help="The distiller used to generate a few shot examples from traj",
    )
    parser.add_argument(
        "--prompt_path",
        type=str,
        default="envs/classic_control/few_shot_examples/cartpole",
        help="The path of prompts",
    )
    parser.add_argument(
        "--prompt_level",
        type=int,
        default=1,
        help="The level of prompts",
    )
    parser.add_argument(
        "--num_trails",
        type=int,
        default=5,
        help="The number of trials",
    )
    parser.add_argument(
        "--use_short_mem",
        type=int,
        default=1,
        help="Whether use short mem",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=100,
        help="set seed",
    )
    parser.add_argument(
        "--short_mem_num",
        type=int,
        default=10,
        help="Set numbers of short memories used in actor, if use_short_mem = 1"
    )
    parser.add_argument(
        "--is_only_local_obs",
        type=int,
        default=1,
        help="Whether only taking local observations, if is_only_local_obs = 1, only using local obs"
    )
    parser.add_argument(
        "--api_type",
        type=str,
        default="openai",
        choices=["azure", "openai"],
        help="choose api type, now support azure and openai"
    )
    args = parser.parse_args()

    if args.api_type != "azure" and args.api_type != "openai":
        raise ValueError(f"The {args.api_type} is not supported, please use 'azure' or 'openai' !")
    
    # Please note when using "azure", the model name is gpt-35-turbo while using "openai", the model name is "gpt-3.5-turbo"
    if args.api_type == "azure":
        if args.gpt_version == "gpt-3.5-turbo":
            args.gpt_version = 'gpt-35-turbo'
    elif args.api_type == "openai":
        if args.gpt_version == "gpt-35-turbo":
            args.gpt_version = 'gpt-3.5-turbo'

    # Get the specified translator, environment, and ChatGPT model
    env_class = envs.REGISTRY[args.env]
    init_summarizer = InitSummarizer(envs.REGISTRY[args.init_summarizer], args)
    curr_summarizer = CurrSummarizer(envs.REGISTRY[args.curr_summarizer])
    
    if args.future_summarizer:
        future_summarizer = FutureSummarizer(
            envs.REGISTRY[args.future_summarizer],
            envs.REGISTRY["cart_policies"],
            future_horizon=args.future_horizon,
        )
    else:
        future_summarizer = None

    decider_class = deciders.REGISTRY[args.decider]
    distiller_class = distillers.REGISTRY[args.distiller]
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

    logfile = (
        f"llm.log/output-{args.env_name}-{args.decider}-{args.gpt_version}-l{args.prompt_level}"
        f"-{datetime.datetime.now().timestamp()}.log"
    )

    logfile_reflexion = (
        f"llm.log/memory-{args.env_name}-{args.decider}-{args.gpt_version}-l{args.prompt_level}"
        f"-{datetime.datetime.now().timestamp()}.log"
    )
    my_distiller = distiller_class(logfile=logfile_reflexion,args=args)

    args.game_description = environment.game_description
    args.goal_description = environment.goal_description
    args.action_description = environment.action_description
    args.action_desc_dict = environment.action_desc_dict
    args.reward_desc_dict = environment.reward_desc_dict

    logger.add(logfile, colorize=True, enqueue=True, filter=lambda x: '[Reflexion Memory]' not in x['message'])

    decider = decider_class(environment.env.action_space, args, prompts_class, my_distiller, temperature=0.0, logger=logger, max_tokens=args.max_generate_tokens)
    # Evaluate the translator
    evaluate_translator(translator, environment, decider, args.max_episode_len, logfile, args)