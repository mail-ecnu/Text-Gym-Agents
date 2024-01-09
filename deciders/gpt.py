import openai
class gpt: 
    def __init__(self, args, api_key=None):
        if args.api_type == "azure":
            openai.api_type = "azure"
            openai.api_version = "2023-05-15"
            # Your Azure OpenAI resource's endpoint value.
            openai.api_base = "https://midivi-main-scu1.openai.azure.com/"
            openai.api_key = api_key
        else:
            openai.api_key = api_key