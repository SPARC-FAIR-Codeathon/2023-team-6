# Import flask and datetime module for showing date and time
from flask import Flask, request, send_file
from prompt import build_prompt, num_tokens_from_string, load_api_key_from_yaml, write_files, load_api_key_from_request
import openai

# Initializing flask app
app = Flask(__name__)


# Post route for running script to generate and return dockerfile
@app.route("/generateFiles", methods=['POST'])
def generate_files():

    prompt = build_prompt(request.json)
    
    num_tokens = num_tokens_from_string(prompt, "cl100k_base")

    print("number of tokens = ", num_tokens)

    # create a chat completion
    messages = [
        {"role": "system", "content": "You are an AI assistant for Team 6"},
        {"role": "user", "content": prompt}
    ]

    # openai.api_key = load_api_key_from_yaml("/creds.yaml")
    openai.api_key = load_api_key_from_request(request.json)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response_text = response.choices[0].message.content

    write_files(response_text)

    return {}

# Download script.py
@app.route('/getScript')
def get_script():
    return send_file('/Users/masonmings/SPARC2/2023-team-6/backend/script.py', download_name='script.py')

# Download Dockerfile
@app.route('/getDockerfile')
def get_dockerfile():
    return send_file('/Users/masonmings/SPARC2/2023-team-6/backend/Dockerfile', download_name='Dockerfile')

# Running app
if __name__ == "__main__":
    app.run(debug=True)
