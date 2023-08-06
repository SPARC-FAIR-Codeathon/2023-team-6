import openai
import subprocess
import os
import tiktoken
import shutil
import tempfile
import yaml
import os
import os.path as path

# load openai api key
def load_api_key_from_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config.get('openai_api_key')

# grab the key, which is outside the repo
two_up = path.abspath(path.join(os.getcwd(),"../../.."))
api_path = two_up + "/creds.yaml"
openai.api_key = load_api_key_from_yaml(api_path)

# import and print
with open("prompt.txt", 'r') as f:
    prompt = f.read()
print(prompt)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens = num_tokens_from_string(prompt, "cl100k_base")

print("number of token = ", num_tokens)

# create a chat completion
messages = [
    {"role": "system", "content": "You are an AI assistant for Team 6"},
    {"role": "user", "content": prompt}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)
response_text = response.choices[0].message.content
print(response_text)