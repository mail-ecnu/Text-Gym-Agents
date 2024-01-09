import envs
import deciders
import distillers
import prompts as task_prompts
import datetime
import time
from envs.translator import InitSummarizer, CurrSummarizer, FutureSummarizer, Translator
import gym
import pandas as pd
import random
import datetime
from loguru import logger
from argparse import Namespace
import gradio as gr
import subprocess
import openai
import os
import shutil
import subprocess
from pathlib import Path
from urllib.request import urlretrieve


def set_seed(seed):
    random.seed(seed)         

def main_progress(
        api_type, openai_key, env_name, decider_name, 
        prompt_level, num_trails, seed
    ):
    init_summarizer = env_name.split("-")[0] + '_init_translator'
    curr_summarizer = env_name.split("-")[0] + '_basic_translator'
    if "Represented" not in init_summarizer:
        init_summarizer = init_summarizer.lower()
        curr_summarizer = curr_summarizer.lower()
    args = Namespace(
        env_name=env_name,
        init_summarizer=init_summarizer,
        curr_summarizer=curr_summarizer,
        decider=decider_name,
        prompt_level=prompt_level,
        num_trails=num_trails,
        seed=seed,
        future_summarizer=None,
        env="base_env",
        gpt_version="gpt-3.5-turbo",
        render="rgb_array",
        max_episode_len=200,
        max_query_tokens=5000,
        max_tokens=2000,
        distiller="traj_distiller",
        prompt_path=None,
        use_short_mem=1,
        short_mem_num=10,
        is_only_local_obs=1,
        api_type=api_type,
    )

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

    decider = decider_class(openai_key, environment.env.action_space, args, prompts_class, my_distiller, temperature=0.0, logger=logger, max_tokens=args.max_tokens)
    
    # Evaluate the translator
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

            # single run
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
            # state_description, prompt, response, action = None, None, None, None
            start_time = datetime.datetime.now()
            # Run the game for a maximum number of steps
            for round in range(args.max_episode_len):
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
                        raise e
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

                # return results
                yield environment.render(), state_description, prompt, response, action

                if termination or truncation:
                    if logger:
                        logger.info(f"Terminated!")
                    break
                time.sleep(5)
            decider.env_history.add(
                'terminate_state', environment.get_terminate_state(round+1, args.max_episode_len))
            decider.env_history.add("cummulative_reward", str(utility))
            # Record the final reward
            if logger:
                logger.info(f"Cummulative reward: {utility}.")
                end_time = datetime.datetime.now()
                time_diff = end_time - start_time
                logger.info(f"Time consumer: {time_diff.total_seconds()} s")
            
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

# def pause():
#     for i in range(31415926):
#         time.sleep(0.1)
#         yield i            

if __name__ == "__main__":

    # Github action test 8

    # install Atari ROMs
    subprocess.run(['AutoROM', '--accept-license'])

    # install mujoco

    # Step 1: Download and set up MuJoCo
    MUJOCO_URL = "https://github.com/google-deepmind/mujoco/releases/download/2.1.0/mujoco210-linux-x86_64.tar.gz"
    MUJOCO_FILENAME = "mujoco210-linux-x86_64.tar.gz"

    # Download MuJoCo
    print("Downloading MuJoCo...")
    urlretrieve(MUJOCO_URL, MUJOCO_FILENAME)

    # Create and move to ~/.mujoco directory
    mujoco_dir = Path.home() / ".mujoco"
    mujoco_dir.mkdir(exist_ok=True)
    shutil.move(MUJOCO_FILENAME, str(mujoco_dir / MUJOCO_FILENAME))

    # Extract the file
    print("Extracting MuJoCo...")
    subprocess.run(["tar", "-zxvf", str(mujoco_dir / MUJOCO_FILENAME)], cwd=mujoco_dir)

    # Edit .bashrc
    bashrc_path = Path.home() / ".bashrc"
    mujoco_path = mujoco_dir / "mujoco210" / "bin"
    export_line = f"export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:{mujoco_path}\n"

    with open(bashrc_path, "a") as bashrc_file:
        bashrc_file.write(export_line)

    # Set LD_LIBRARY_PATH for the current process
    ld_lib_path = os.environ.get("LD_LIBRARY_PATH", "")
    new_ld_lib_path = f"{ld_lib_path}{mujoco_path}"
    os.environ["LD_LIBRARY_PATH"] = new_ld_lib_path

    # Step 2: Install gym[mujoco]
    print("Installing gym[MuJoCo]...")
    subprocess.run(["pip", "install", "gym[mujoco]"])

    # # Set render
    os.environ["MUJOCO_GL"] = "egl"
    # os.environ["DISPLAY"] = ":0"
    # print(f'LD_LIBRARY_PATH: {os.environ["LD_LIBRARY_PATH"]}')
    # assert os.path.exists(str(mujoco_path))
    # subprocess.run("cp -r /home/user/.mujoco/mujoco210/bin/* /usr/lib/", shell=True)
    # import mujoco_py
    # flag = 'gpu' in str(mujoco_py.cymj).split('/')[-1]
    # print(f'flag: {flag}')
    # if not flag:
    #     ld_lib_path = os.environ.get("LD_LIBRARY_PATH", "")
    #     new_ld_lib_path = f"{ld_lib_path}:/usr/lib/nvidia-000"
    #     os.environ["LD_LIBRARY_PATH"] = new_ld_lib_path
    #     subprocess.run(["sudo", "mkdir", "-p", "/usr/lib/nvidia-000"])
    #     assert 'gpu' in str(mujoco_py.cymj).split('/')[-1]


    custom_css = """
        #render {
            flex-grow: 1;
        }
        #input_text .tabs {
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        #input_text .tabitem[style="display: block;"] {
            flex-grow: 1;
            display: flex !important;
        }
        #input_text .gap {
            flex-grow: 1;
        }
        #input_text .form {
            flex-grow: 1 !important;
        }
        #input_text .form > :last-child{
            flex-grow: 1;
        }
    """

    with gr.Blocks(theme=gr.themes.Monochrome(), css=custom_css) as demo:
        with gr.Row():
            api_type = gr.Dropdown(["azure", "openai"], label="API Type", scale=1)
            openai_key = gr.Textbox(label="OpenAI API Key", type="password", scale=3)
        with gr.Row():
            env_name = gr.Dropdown(
                ["CartPole-v0",
                 "LunarLander-v2",
                 "Acrobot-v1",
                 "MountainCar-v0",
                 "Blackjack-v1",
                 "Taxi-v3",
                 "CliffWalking-v0",
                 "FrozenLake-v1",
                 "MountainCarContinuous-v0",
                 "Ant-v4",
                 "HalfCheetah-v4",
                 "Hopper-v4",
                 "Walker2d-v4",
                 "Swimmer-v4",
                 "Reacher-v4",
                 "Pusher-v4",
                 "RepresentedBoxing-v0", 
                 "RepresentedPong-v0", 
                 "RepresentedMsPacman-v0", 
                 "RepresentedMontezumaRevenge-v0"], 
                label="Environment Name")
            decider_name = gr.Dropdown(
                ["naive_actor", 
                 "cot_actor", 
                 "spp_actor", 
                 "reflexion_actor"], 
                 label="Decider")
            # prompt_level = gr.Dropdown([1, 2, 3, 4, 5], label="Prompt Level")
            # TODO: support more prompt levels
            prompt_level = gr.Dropdown([1, 3], label="Prompt Level")
        with gr.Row():
            num_trails = gr.Slider(1, 100, 1, label="Number of Trails", scale=2)
            seed = gr.Slider(1, 1000, 1, label="Seed", scale=2)
            run = gr.Button("Run", scale=1)
            # pause_ = gr.Button("Pause")
            # resume = gr.Button("Resume")
            stop = gr.Button("Stop", scale=1)
        with gr.Row():
            with gr.Column():
                render = gr.Image(label="render", elem_id="render")
            with gr.Column(elem_id="input_text"):
                state = gr.Textbox(label="translated state")
                prompt = gr.Textbox(label="prompt", max_lines=20)
        with gr.Row():
            response = gr.Textbox(label="response")
            action = gr.Textbox(label="parsed action")
        run_event = run.click(
            fn=main_progress, 
            inputs=[
                api_type, openai_key, env_name, 
                decider_name, prompt_level, num_trails, seed], 
            outputs=[render, state, prompt, response, action])
        stop.click(fn=None, inputs=None, outputs=None, cancels=[run_event])
        # pause_event = pause_.click(fn=pause, inputs=None, outputs=None)
        # resume.click(fn=None, inputs=None, outputs=None, cancels=[pause_event])

    demo.launch()