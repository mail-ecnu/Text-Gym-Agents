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
