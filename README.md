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
    def __init__(self,):
        openai.api_type = "azure"
        openai.api_version = "2023-05-15"
        # Your Azure OpenAI resource's endpoint value.
        openai.api_base = "https://js-partner.openai.azure.com/"
        openai.api_key = "your azure openai key"
```

2. Install Requirements

```
conda env create --file environment.yml
```

3. Testing 
The project can be run using the provided test.sh script. This script runs a series of commands, each of which initiates a Gym environment and applies different translators to it.

Here is an example of how to run the script:

```
./test.sh
```
The commands in test.sh are structured as follows:

```
python main.py --env_name ENV_NAME --init_summarizer INIT_SUMMARIZER --curr_summarizer CURR_SUMMARIZER [--future_summarizer FUTURE_SUMMARIZER --future_horizon FUTURE_HORIZON] 
```
Where:

* ENV_NAME: The name of the Gym environment to be used (e.g., CartPole-v0).
* INIT_SUMMARIZER: The initial summarizer to be used (e.g., cart_init_translator).
* CURR_SUMMARIZER: The current summarizer to be used (e.g., cart_basic_translator).
* FUTURE_SUMMARIZER (optional): The future summarizer to be used (e.g., cart_basic_translator).
* FUTURE_HORIZON (optional): The horizon that each policy will look to (e.g., 3).

## Supported Environment Translators and LLM Deciders

|                              |          Acrobot         |              Cart Pole             |       Mountain Car       |         Pendulum         |       Lunar Lander       |         Blackjack        |           Taxi           |       Cliff Walking      |        Frozen Lake       |
|------------------------------|:------------------------:|:----------------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|:------------------------:|
| Translator                   | :heavy_multiplication_x: |         :white_check_mark:         | :heavy_multiplication_x: | :heavy_multiplication_x: |    :white_check_mark:    | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: | :heavy_multiplication_x: |
| Chain-of-Thought             |    :heavy_minus_sign:    | :white_check_mark:(L1)<br>:gift:<sup>[1]</sup>(~30) |    :heavy_minus_sign:    |    :heavy_minus_sign:    | :white_check_mark:(L1)<br/>:gift:<sup>[1]</sup>(-367) |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |
| Program-aided Language Model |    :heavy_minus_sign:    | :white_check_mark:(L1)<br>:gift:(168) |    :heavy_minus_sign:    |    :heavy_minus_sign:    |        :white_check_mark:(L1)<br/>:gift:(-68)         |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |
| Self-ask Prompting           |    :heavy_minus_sign:    | :white_check_mark:(L1)<br>:gift:(~10) |    :heavy_minus_sign:    |    :heavy_minus_sign:    | :heavy_multiplication_x: |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |
| Self-consistency Prompting   |    :heavy_minus_sign:    |      :white_check_mark:(L1)<br>:gift:(~30)      |    :heavy_minus_sign:    |    :heavy_minus_sign:    | :heavy_multiplication_x: |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |
| Reflexion                    |    :heavy_minus_sign:    |      :heavy_multiplication_x:      |    :heavy_minus_sign:    |    :heavy_minus_sign:    | :heavy_multiplication_x: |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |    :heavy_minus_sign:    |
| Solo Performance Prompting | :heavy_minus_sign: | :white_check_mark:(L1)<br/>:gift:(43) | :heavy_minus_sign: | :heavy_minus_sign: | :white_check_mark:(L1)<br/>:gift:(-583) | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: |

<sup>[1]: Cumulative reward.</sup>
![Image text](https://github.com/mail-ecnu/LLM-Decider-Bench/blob/master/vis/Classic%20Control.png)
![Image text](https://github.com/mail-ecnu/LLM-Decider-Bench/blob/master/vis/Box%202D.png)
![Image text](https://github.com/mail-ecnu/LLM-Decider-Bench/blob/master/vis/Toy%20Text.png)

>
> 1. Except for the reflexion L3 decider, all other L3 deciders in this task do not have memory.
> 2. reflexion L1 and L3 both have memory.
> 3. reflexion L1 run 5 trails.
> 4. Blackjack、MountainCar、Cliffwalking(PAL)、CartPole(PAL)、Taxi(SPP、PAL)、Frozen Lake use deciders modified at 15:29 09.18
> 5. update Frozen Lake translator, add prior knowledge. 
# Remarks 
1. how to use future info 
We provide future info in the env_info part. It is a dict and you can convert it to a text further to make your agent aware the world model. 
