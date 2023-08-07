import openai
import os
import tiktoken
import yaml
import os.path as path
import re

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

print("number of tokens = ", num_tokens)

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

# write the response to a file
with open("response.txt", "w") as file:
    file.write(response_text)

# Define patterns for each section
py_pattern = r'script\.py:(?:\s*```)?\s*(.*?)\s*```'
docker_pattern = r'Dockerfile:(?:\s*```)?\s*(.*?)\s*```'

# Extract content for each file using regular expressions
py_content = re.search(py_pattern, response_text, re.DOTALL)
docker_content = re.search(docker_pattern, response_text, re.DOTALL)

# Write the content to respective files if the content was found

if py_content:
    with open("script.py", "w") as file2:
        # remove the word "python" since it is difficult to do with a prompt
        py_content2 = py_content.group(1).strip().replace('python', '')
        file2.write(py_content2)

if docker_content:
    with open("Dockerfile", "w") as file3:
        file3.write(docker_content.group(1).strip())