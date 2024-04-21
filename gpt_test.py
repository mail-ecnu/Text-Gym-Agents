# This file contains functions for interacting with the ChatGPT model

import openai
from deciders.gpt import gpt 
import argparse
from loguru import logger
from deciders.parser import DISPARSERS, CONPARSERS
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from memory.env_history import EnvironmentHistory
import tiktoken
import json
import re
from deciders.utils import run_chain, get_completion, get_chat
from gym.spaces import Discrete
model = "gpt-3.5-turbo"
class GPTTest(gpt):
    def __init__(self, args):
        super().__init__(args)
        chat = ChatOpenAI(temperature=1.0, base_url=openai.base_url, openai_api_key=openai.api_key, model=model)
        from openai import OpenAI
        client =  OpenAI(
            api_key=openai.api_key,
            base_url=openai.base_url,
        )
        prompt = "Hello"
        print(f"prompt is {prompt}")
        res = get_chat(client, prompt, api_type=args.api_type, model=model, temperature=1.0, max_tokens=256)

parser = argparse.ArgumentParser(
        description="Evaluate a translator in a gym environment with a ChatGPT model."
    )
parser.add_argument(
        "--api_type",
        type=str,
        default="openai",
    )
args = parser.parse_args()
gpt_test = GPTTest(args)