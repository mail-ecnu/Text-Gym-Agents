# Bench LLM Deciders with gym translators 
This project provides a set of translators to convert OpenAI Gym environments into text-based environments. It is designed to investigate the capabilities of large language models in decision-making tasks within these text-based environments.

## Summarizer Levels
We translate the game with basic level descriptions. It provides a simple description of the current state of the game. It's suitable for beginners who are just getting familiar with the game.
## Environment Categories
The environments are categorized based on the information that revealed to agents. We propose *5 level* scenarios. 

**L1**: No external information is given. Only abstract game description. (zero shot)

**L2**: Agents can take a sampling traj of the random policy as external knowledge. (few shots, off-policy info)

**L3**: self sampling and updating w/ feedback. (few shots, on-policy info)

**L4**: sampling traj of an expert policy (few shots, expert-info)

**L5**: expert teaching (few shots, expert-info with guidance)

The five level scenarios are mainly considering making decision with perception. For future world, we leave it to stage 2 investigation.

**Perception and Future World**: These environments provide a perception of the current state, and also predict future infos. The futrue info is given in the info dict at step and reset.

It should be noted that the past memory part should be implemented as a component of deciders. 

## Fewshot Examples Generation
For `L1` level, the `[]` is given.
For `L2` and `L4` level, we use `gen_few_shots_examples.py` to generate corresponding examples in json format and place them in the `envs/*/few_shot_examples/`.
For `L3` level, agent should collect the examples on their own and only a few methods support it. Thus we leave it to the agent design. 
For `L5` level, we handcraft the few shot examples with domain knowledge in `prompts/task_relevant`.

## Usage 

1. create `./deciders/gpt.py` to provide your gpt agent: 
```python 
import openai
class gpt: 
    def __init__(self, args):
        if args.api_type == "azure":
            openai.api_type = "azure"
            openai.api_version = "2023-05-15"
            # Your Azure OpenAI resource's endpoint value.
            openai.api_base = "https://midivi-main-scu1.openai.azure.com/"
            openai.api_key = "your azure key"
        else:
            openai.api_key = "your openai key"
```
2. Install Requirements

```
conda env create --file environment.yaml
```

3. Testing 
The project can be run using the provided .sh script in shell/ folder. This script runs a series of commands, each of which initiates a Gym environment and applies different translators to it.

Here is an example of how to run the script:

```
sh shell/test_cartpole.sh
```
Or you can also test this by copying a command from a .sh script
```
python main_reflexion.py --env_name CartPole-v0 --init_summarizer cart_init_translator --curr_summarizer cart_basic_translator --decider exe_actor --prompt_level 1 --num_trails 1 --distiller guide_generator 
```

If you use openai key, please add "--api_type openai" at the end of the command!

### Install Mujoco Environment
1. Download the MuJoCo, recommand [mujoco210](https://github.com/google-deepmind/mujoco/releases/tag/2.1.0), for Linux, it is `mujoco210-linux-x86_64.tar.gz
`, then
- make new file `mkdir ~/.mujoco`
- move the dowload file into the file `cp mujoco210-linux-x86_64.tar.gz ~/.mujoco` and extract it by `tar -zxvf mujoco210-linux-x86_64.tar.gz` 
- `vim ~/.bashrc` and add the following line into the `.bashrc`:
`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/<user>/.mujoco/mujoco210/bin
`

2. install mujoco_py which allows using MuJoCo from Python 
```
sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3
sudo apt-get install libglew-dev

pip install mujoco-py==2.1.2.14
pip install cython==0.29.37
```

3. install gym[mujoco]
`pip install gym[mujoco]`

### Import Atari ROMs

If you encounter the error `Unable to find game "[env_name]"` when running a script for Atari environments, it may be due to the absence of Atari ROMs in the `atari_py` package since version 0.2.7. To resolve this issue, you can manually download the ROMs and add them to Gym's registry.

``` shell
pip install gym[accept-rom-license]
AutoROM --accept-license
```

Test  with the following code

```python
import gym
from atariari.benchmark.wrapper import AtariARIWrapper

# Initialize the environment
env = AtariARIWrapper(gym.make("MsPacmanNoFrameskip-v4"))
obs = env.reset()

# Perform a single step in the environment
obs, reward, done, info = env.step(1)

# Check the information provided by the environment (including labels and scores)
print(info["labels"])
```

If everything runs smoothly, you have successfully imported the Atari ROMs and set up your environment.

Reference: [StackOverflow answer](https://stackoverflow.com/a/68143504/38626)

### Visulization with Gradio

> Gradio is an open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitary Python function. You can then share a link to your demo or web application in just a few seconds using Gradio’s built-in sharing features. No JavaScript, CSS, or web hosting experience needed! [from https://www.gradio.app/guides/quickstart]

Prerequisite: Gradio requires Python 3.8 or higher

Run this in your terminal or command prompt:

```shell
pip install gradio
```

And then run the following Python file in the root directory:

```shell
python gradio_reflexion.py
```

The visulization web application will open in a browser on http://server-ip-address:7860 if running from a file. If you are running within a notebook, the demo will appear embedded within the notebook.