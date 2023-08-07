import os
import tiktoken
import yaml
import os.path as path
import re
import uuid

###############################
# get the ChatGPT API key
###############################

def load_api_key_from_yaml(relative_file_path):
    # grab the key, which is outside the repo
    two_up = path.abspath(path.join(os.getcwd(),"../../"))
    api_path = two_up + relative_file_path

    with open(api_path, 'r') as file:
        config = yaml.safe_load(file)
        return config.get('openai_api_key')



###############################
# engineer the ChatGPT prompt
###############################

# format the final prompt
def build_prompt(params):
    packages = ""
    for package in params['packages']:
        packages += package + ", "
    packages = packages[0:-2]

    prompt = f"""
    Create the code for two files: (1) a Python script to load and run {params['problem']} using the {params['fileType']} formatted files in the "data" folder; and (2) a Dockerfile to create a Docker image to contain the necessary Python packages for the analysis. Make section headers in your output: "script.py" and "Dockerfile". Do not include the words python, Python, dockerfile, or Dockerfile in code for these files.

    Specific instructions for creating the Python script:
    Name the script "script.py". Use the following list of additional Python packages: {packages}. Name the analysis results file "results.txt" and place it in the "results" folder. Include the following code at the bottom of the script to record versions of packages in the Docker container.

    import subprocess
    with open("requirements.txt", "w") as f:
        subprocess.run(["pip", "freeze"], stdout=f)

    Specific instructions for creating the Dockerfile:
    If this is needed for the Dockerfile, the current package install name for sci-kit learn is "scikit-learn". Copy the Python script into the image so that the script will run automatically when the container is created. Do not include a maintainer label and install the Python packages internally and do not use a "requirements.txt" file to do this. Make sure that that the python script running inside the container has access to the data file(s) by mounting the host provided directory in docker run to the "/app" directory inside the container, which will also be where the "results" and "data" folders are located. Do not use the Dockerfile COPY command to copy the dataset.

    A description of the data contained in the "data" folder is pasted below:
    {params['datasetDescription']}
    """

    return prompt


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Define docker section pattern and extract contents
def get_docker_content(response_text):
    docker_pattern = r'Dockerfile:(?:\s*```)?\s*(.*?)\s*```'
    return re.search(docker_pattern, response_text, re.DOTALL)

# Define content section pattern and extract contents
def get_py_content(response_text):
    py_pattern = r'script\.py:(?:\s*```)?\s*(.*?)\s*```'
    return re.search(py_pattern, response_text, re.DOTALL)

def write_files(response_text):
    docker_content = get_docker_content(response_text)
    py_content = get_py_content(response_text)

    # Write the content to respective files if the content was found
    if py_content:
        with open("script.py", "w") as file2:
            # remove the word "python" since it is difficult to do with a prompt
            py_content2 = py_content.group(1).strip().replace('python', '')
            file2.write(py_content2)
    if docker_content:
        with open("Dockerfile", "w") as file3:
            file3.write(docker_content.group(1).strip())
