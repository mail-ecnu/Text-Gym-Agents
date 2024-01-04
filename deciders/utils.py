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
def get_completion(prompt: str, api_type: str = "azure", engine: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, stop_strs: Optional[List[str]] = None) -> str:
    if api_type == "azure":
        response = openai.Completion.create(
                    engine=engine,
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=stop_strs,
                    # request_timeout = 1
                )
        return response.choices[0].text
    elif api_type == "openai":
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        response = openai.ChatCompletion.create(
            model=engine,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            # request_timeout = 1
        )
        return response.choices[0]["message"]["content"]

# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_chat(prompt: str, api_type: str = "azure", model: str = "gpt-35-turbo", engine: str = "gpt-35-turbo", temperature: float = 0.0, max_tokens: int = 256, stop_strs: Optional[List[str]] = None, is_batched: bool = False) -> str:
    assert model != "text-davinci-003"
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    if api_type == "azure":
        response = openai.ChatCompletion.create(
            model=model,
            engine=engine,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            # request_timeout = 1
        )
        return response.choices[0]["message"]["content"]
    elif api_type == "openai":
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            # request_timeout = 1
        )
        return response.choices[0]["message"]["content"]

