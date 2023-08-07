# AI Workflows for SPARC

## What is AI Workflows for SPARC?
This project consists of a dashboard implemented with React (frontend) and Flask (backend) that allows users to select relevant datasets from the SPARC data repository along with desired analysis to be performed on the data. The data is retreived via the Pennsieve API and downloaded locally to the user's computer. The requested analysis is used to generate a prompt that is then sent to ChatGPT via the OpenAI API, which in turn generates a Dockerfile and Python script that is returned to the user. The user runs the Dockerfile to create a Docker image with the appropriate analysis environment and the Python script is used to complete the data analysis.

## Requirements
* [OpenAI](https://openai.com/) API Key for ChapGPT
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Installation
[TODO] How is the dashboard installed?

The code requires a yaml file containing the user's OpenAI API key, named "creds.yaml", be placed directly outside the git repo.

## Instructions for Use
[TODO] Include more details about using the dashboard.

[TODO] Include more information about the options for analysis tools.

1. Create a local folder for the analysis that will contain the selected dataset(s) and files downloaded from the Dashboard.
2. Using the dashboard, select and download data to the local folder (a sub-folder in this location, named "data", will contain the data).
3. Using the dashboard, select the type of analysis and create the custom Python script and Dockerfile.

[TODO] Is there a `Docker build` step to build the image before running it?

4. In the command line interface (CLI), navigate to the local folder and obtain the \<absolute path\> by running `pwd` in most Unix shells (Linux/MacOS), `cd` in Windows Command Prompt, or `Get-Location` in Windows PowerShell. Then run the following command to create the Docker image and run the analysis, which will produce a sub-folder, named "results":
    ```
    docker run -v <absolute path>:/app ml_analysis_image_api:latest
    ```
5. To stop the Docker container, first, run the following in the CLI to determine the container name:
    ```
    docker ps -a
    ```
6. Next, run the following to stop the container:
    ```
    docker rm <container name>
    ```
7. To delete the Docker image run the following in the CLI:
    ```
    docker rmi ml_analysis_image_api:latest
    ```

## [SPARC FAIR Codeathon 2023](https://sparc.science/news-and-events/events/2023sparc-codeathon) — Team 6
**Team members:**
* Charles Horn
* John Bentley
* Mason Mings

## License
AI Workflows for SPARC is distributed under the [MIT License](https://opensource.org/license/mit/).

2023

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
