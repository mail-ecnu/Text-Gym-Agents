import os
import sys
import tiktoken
import openai 
from tenacity import (
    retry,
    stop_after_attempt, # type: ignore
    wait_random_exponential, # type: ignore
)

from typing import Optional, List


# from .gpt import gpt
# gpt().__init__()
def num_tokens_from_string(model, string) -> int:
    """Returns the number of tokens in a text string."""
    if model == 'Meta-Llama-3-8B-Instruct':
        model = 'gpt-3.5-turbo'
    enc = tiktoken.encoding_for_model(model)
    num_tokens = len(enc.encode(str(string)))
    return num_tokens

import timeout_decorator
@timeout_decorator.timeout(30)
def run_chain(chain, *args, **kwargs):
    return chain.run(*args, **kwargs)

def get_completion(client, prompt: str, api_type: str = "azure", engine: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, stop_strs: Optional[List[str]] = None) -> str:
    if api_type == "azure":
        response = client.completions.create(
            model=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=stop_strs,
        )

    elif api_type == "openai":
        
        response = client.completions.create(
            model=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            # request_timeout = 1
        )
        
    elif api_type == "vllm":
        response = client.completions.create(
            model=engine,
            prompt=prompt,
            stop=["<|im_end|>"],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
    return response.choices[0].text

def get_chat(client, messages: list, api_type: str = "azure", model: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, seed: int = 1, stop_strs: Optional[List[str]] = None, is_batched: bool = False) -> str:
    assert model != "text-davinci-003"
    if api_type == "azure":
        if model == "gpt-35-turbo":
            model = "gpt-3.5-turbo"
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=stop_strs,
        )
    elif api_type == "openai":
        response = client.chat.completions.create(
            temperature=temperature,
            seed=seed
            # request_timeout = 1
        )
    elif api_type == "openai":
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            seed=seed
            # request_timeout = 1
        )
    elif api_type == "vllm":
        if model == 'Meta-Llama-3-8B-Instruct':
            stop_token = "<|eot_id|>"
        else:
            stop_token = "<|im_end|>"
        # import pdb; pdb.set_trace()
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stop=[stop_token],
            max_tokens=max_tokens,
            temperature=temperature,
            # extra_body={"guided_json": True,}
        )
    usgae = response.usage
    total_token, cost = openai_api_calculate_cost(usgae, model)
    return response.choices[0].message.content, {"token": total_token, "cost": cost}


def openai_api_calculate_cost(usage, model="gpt-4-1106-preview"):
    pricing = {
        'gpt-3.5-turbo-1106': {
            'prompt': 0.001,
            'completion': 0.002,
        },
        'gpt-4-1106-preview': {
            'prompt': 0.01,
            'completion': 0.03,
        },
        'gpt-4': {
            'prompt': 0.03,
            'completion': 0.06,
        }, 
        'gpt-3.5-turbo': {
            'prompt': 0.001,
            'completion': 0.002,
        },
        'gpt-35-turbo': {
            'prompt': 0.001,
            'completion': 0.002,
        },
        'gpt-3.5-turbo-0125': {
            'prompt': 0.0005,
            'completion': 0.0015 ,
        },
        'Meta-Llama-3-8B-Instruct': {
            'prompt': 0.0001,
            'completion': 0.0001,
        }
    }
    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Invalid model specified")
    total_token = usage.total_tokens
    prompt_cost = usage.prompt_tokens * model_pricing['prompt'] / 1000
    completion_cost = usage.completion_tokens * model_pricing['completion'] / 1000

    total_cost = prompt_cost + completion_cost
    total_cost = round(total_cost, 6)

    return total_token, total_cost