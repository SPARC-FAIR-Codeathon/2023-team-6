import openai
import os
import tiktoken
import yaml
import os.path as path
import re

###############################
# get the ChatGPT API key
###############################

def load_api_key_from_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config.get('openai_api_key')

# grab the key, which is outside the repo
two_up = path.abspath(path.join(os.getcwd(),"../"))
api_path = two_up + "/creds.yaml"

openai.api_key = load_api_key_from_yaml(api_path)

###############################
# engineer the ChatGPT prompt
###############################

# import user variables
with open("user_input.yaml", "r") as file:
    user_content = yaml.safe_load(file)

# format the final prompt
prompt = f"""
Create the code for two files: (1) a Python script to load and run {user_content['analysis_type']} using the {user_content['file_type']} formatted files in the "data" folder; and (2) a Dockerfile to create a Docker image to contain the necessary Python packages for the analysis. Make section headers in your output: "script.py" and "Dockerfile". Do not include the words python, Python, dockerfile, or Dockerfile in code for these files.

Specific instructions for creating the Python script:
Name the script "script.py". Use the following list of additional Python packages: {user_content['python_packages']}. Name the analysis results file "results.txt" and place it in the "results" folder. Include the following code at the bottom of the script to record versions of packages in the Docker container.

import subprocess
with open("requirements.txt", "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f)

Specific instructions for creating the Dockerfile:
If this is needed for the Dockerfile, the current package install name for sci-kit learn is "scikit-learn". Copy the Python script into the image so that the script will run automatically when the container is created. Do not include a maintainer label and install the Python packages internally and do not use a "requirements.txt" file to do this. Make sure that that the python script running inside the container has access to the data file(s) by mounting the host provided directory in docker run to the "/app" directory inside the container, which will also be where the "results" and "data" folders are located. Do not use the Dockerfile COPY command to copy the dataset.

A description of the data contained in the "data" folder is pasted below:
{user_content['dataset_description']}
"""

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

# make a results file folder
folder_name = "results"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Write the content to respective files if the content was found
if py_content:
    with open("script.py", "w") as file2:
        # remove the word "python" since it is difficult to do with a prompt
        py_content2 = py_content.group(1).strip().replace('python', '')
        file2.write(py_content2)
if docker_content:
    with open("Dockerfile", "w") as file3:
        file3.write(docker_content.group(1).strip())