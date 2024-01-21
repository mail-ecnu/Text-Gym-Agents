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
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


Model = Literal["gpt-4", "gpt-35-turbo", "text-davinci-003"]

# from .gpt import gpt
# gpt().__init__()
def num_tokens_from_string(model, string) -> int:
    """Returns the number of tokens in a text string."""
    enc = tiktoken.encoding_for_model(model)
    num_tokens = len(enc.encode(str(string)))
    return num_tokens

import timeout_decorator
@timeout_decorator.timeout(30)
def run_chain(chain, *args, **kwargs):
    return chain.run(*args, **kwargs)


def get_chat(messages: list, api_type: str = "azure", model: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, seed: int = 1, stop_strs: Optional[List[str]] = None, is_batched: bool = False) -> str:
    assert model != "text-davinci-003"
    if api_type == "azure":
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
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
        'gpt-35-turbo': {
            'prompt': 0.001,
            'completion': 0.002,
        },
    }
    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Invalid model specified")
    total_token = usage.total_tokens
    prompt_cost = usage.prompt_tokens * model_pricing['prompt'] / 1000
    completion_cost = usage.completion_tokens * model_pricing['completion'] / 1000

    total_cost = prompt_cost + completion_cost
    # round to 6 decimals
    total_cost = round(total_cost, 6)

    # print(f"\nTokens used:  {usage.prompt_tokens:,} prompt + {usage.completion_tokens:,} completion = {usage.total_tokens:,} tokens")
    # print(f"Total cost for {model}: ${total_cost:.4f}\n")

    return total_token, total_cost