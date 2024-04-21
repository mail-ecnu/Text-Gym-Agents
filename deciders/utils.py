import os
import sys
import openai # 0.27.8
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

import timeout_decorator
@timeout_decorator.timeout(30)
def run_chain(chain, *args, **kwargs):
    return chain.run(*args, **kwargs)

# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
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

# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_chat(client, prompt: str, api_type: str = "azure", model: str = "gpt-35-turbo", engine: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, stop_strs: Optional[List[str]] = None, is_batched: bool = False) -> str:
    assert model != "text-davinci-003"
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    if api_type == "azure":
        response = client.chat.completions.create(
            model=engine,
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
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
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
        )
    return response.choices[0].message.content

