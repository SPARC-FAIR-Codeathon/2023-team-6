# AI Workflows for SPARC

## What is AI Workflows for SPARC?
This project consists of a dashboard implemented with React (frontend) and Flask (backend) that allows users to select relevant datasets from the SPARC data repository along with desired analyses to be performed on the data. The data is retreived via the Pennsieve API and downloaded locally to the user's computer. The requested analyses is used to generate a prompt that is then sent to ChatGPT via the OpenAI API, which in turn generates a Dockerfile and Python script that is returned to the user. The user runs the Dockerfile to create a Docker image with the appropriate analysis environment and the Python script is used to complete the data analyses.

## Requirements
* OpenAI API Key for ChapGPT
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Installation
[TODO]How is the dashboard installed?

## Instructions for Use

* (1) create a local folder for the analysis that will contain the data and files downloaded from the Dashboard
* (2) using the dashboard, select and download data to the local folder (a sub-folder in this location, "data", will contain the data)
* (3) using the dashboard, select the type of analysis and create the custom Python script and Dockerfile
* (4) in the CLI, navigate to the local folder and obtain the \<absolute path\> by running `pwd` on Linux/MacOS or `cd` on Windows; then run the following command to create the docker image and run the analysis, which will produce a sub-folder, "results"
```
docker run -v <absolute path>:/app ml_analysis_image_api:latest
```
* (5) in the CLI, to stop the Docker container, first, run the following to determine the container name
```
docker ps -a
```
* (6) next, run the following to stop the container
```
docker rm <container name>
```
* (7) in the CLI, to delete the Docker image run
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
