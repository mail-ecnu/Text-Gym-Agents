import os
import sys
import tiktoken
import openai 
from tenacity import (
    retry,
    stop_after_attempt, # type: ignore
    wait_random_exponential, # type: ignore
)

def preprocess_messages(messages):
    ori_msg_cnt = 1
    msg_cnt = 1
    new_messages = []   
    while ori_msg_cnt < len(messages)+1:
        message = messages[ori_msg_cnt-1]
        if msg_cnt%2==1:
            if 'user' in message["role"] or 'user' in message["name"]:
                message["role"] = "user" 
                new_messages.append(message)
                ori_msg_cnt += 1
            elif  'name' in message.keys() and 'user' in message["name"]: 
                message["role"] = "user" 
                new_messages.append(message)
                ori_msg_cnt += 1
            else:
                new_messages.append({"role": "user", "content": " "})
        elif msg_cnt%2==0 :
            if "assistant" in message["role"] or 'assistant' in message["name"]:
                message["role"] = "assistant"
                new_messages.append(message)
                ori_msg_cnt += 1
            elif 'name' in message.keys() and 'assistant' in message["name"]:
                message["role"] = "assistant"
                new_messages.append(message)
                ori_msg_cnt += 1
            else:
                new_messages.append({"role": "assistant", "content": " "})
        msg_cnt += 1
    if msg_cnt%2==1:
        new_messages.append({"role": "user", "content": "Anwser the question."}) 
    return  new_messages

def preprocess_nvidia_messages(messages):
    ori_msg_cnt = 1
    msg_cnt = 1
    new_messages = []   
    while ori_msg_cnt < len(messages)+1:
        message = messages[ori_msg_cnt-1]
        if 'user' in message["role"]:
            message["role"] = "user" 
        elif  'name' in message.keys() and 'user' in message["name"]: 
            message["role"] = "user" 
        elif "assistant" in message["role"]:
            message["role"] = "assistant"
        elif  'name' in message.keys() and 'assistant' in message["name"]:
            message["role"] = "assistant"
        new_messages.append(message)
        ori_msg_cnt += 1
    return  new_messages

class NewResponse:
    def __init__(self, response, is_dashscope=False):
        if is_dashscope:
            self.choices = [Choice(response['output']['choices'][0]['message'].content)]
            self.usage = response['usage']
        else: 
            self.choices = [Choice(response['body']['result'])]
            self.usage = response['body']['usage']

class Choice:
    def __init__(self, content):
        self.message = Message(content)

class Message:
    def __init__(self, content):
        self.content = content

from typing import Optional, List


# from .gpt import gpt
# gpt().__init__()
def num_tokens_from_string(model, string) -> int:
    """Returns the number of tokens in a text string."""
    if model == 'Meta-Llama-3-8B-Instruct' or model=='qwen-long':
        model = 'gpt-3.5-turbo'
    try: 
        enc = tiktoken.encoding_for_model(model)
    except: 
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
    elif api_type in ["openai"]:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=temperature,
            seed=seed
        )
    elif api_type in ["nvidia"]:
        new_messages = preprocess_nvidia_messages(messages)
        # print(new_messages)
        # breakpoint()
        response = client.chat.completions.create(
            model=model,
            messages=new_messages,
            max_tokens=max_tokens,
            stop=stop_strs,
            temperature=max(temperature, 1e-5),
            seed=seed
        )
    elif api_type in ["aistudio"]:
        new_messages = preprocess_messages(messages)
        response_dict = client.do(
            messages=new_messages,
            max_tokens=max_tokens,
            temperature=max(temperature, 1e-5),
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        response = NewResponse(response_dict)

    elif api_type in ["vllm", 'qwen', 'groq'] :
        if model == 'Meta-Llama-3-8B-Instruct':
            stop_token = "<|eot_id|>"
        else:
            stop_token = "<|im_end|>"
        if model == "llama3-70b-instruct" and api_type == "qwen":
            new_messages = preprocess_messages(messages)
            import time
            time.sleep(1)
            response_dict = client.Generation.call(
                model=model,
                messages=new_messages,
                stop=[stop_token],
                max_tokens=max_tokens,
                temperature=max(temperature, 1e-5),
                # extra_body={"guided_json": True,}
                result_format='message',  
            )
            response_dict['usage']['total_tokens'] = response_dict['usage']['input_tokens'] + response_dict['usage']['output_tokens']
            response = NewResponse(response_dict, is_dashscope=True)   
        else: 
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
    # pricing = {
    #     'gpt-3.5-turbo-1106': {
    #         'prompt': 0.001,
    #         'completion': 0.002,
    #     },
    #     'gpt-4-1106-preview': {
    #         'prompt': 0.01,
    #         'completion': 0.03,
    #     },
    #     'gpt-4': {
    #         'prompt': 0.03,
    #         'completion': 0.06,
    #     }, 
    #     'gpt-3.5-turbo': {
    #         'prompt': 0.001,
    #         'completion': 0.002,
    #     },
    #     'gpt-35-turbo': {
    #         'prompt': 0.001,
    #         'completion': 0.002,
    #     },
    #     'gpt-3.5-turbo-0125': {
    #         'prompt': 0.0005,
    #         'completion': 0.0015 ,
    #     },
    #     'Meta-Llama-3-8B-Instruct': {
    #         'prompt': 0.0001,
    #         'completion': 0.0001,
    #     }
    # }
    # try:
    #     model_pricing = pricing[model]
    # except KeyError:
    #     raise ValueError("Invalid model specified")
    try:
        total_token = usage.total_tokens
    except: 
        total_token = usage['total_tokens']
    # prompt_cost = usage.prompt_tokens * model_pricing['prompt'] / 1000
    # completion_cost = usage.completion_tokens * model_pricing['completion'] / 1000

    # total_cost = prompt_cost + completion_cost
    # total_cost = round(total_cost, 6)

    return total_token, -1