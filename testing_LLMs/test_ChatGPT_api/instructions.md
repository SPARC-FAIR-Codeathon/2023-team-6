# steps to reproduce (all commands are executed from the current folder)
* (1) initial files: "prompt.py", "prompt.txt", and "regression_dataset.csv"
* (2) run from CLI:
```
python3 prompt.py
```
* (3) after "script.py" and "Dockerfile" are created automatically, run from CLI:
```
docker build -t ml_analysis_image_api .
```
* (4) run the following to complete the analysis (use "pwd" to get absolute path on Linux/MacOS)
```
docker run -v <absolute path>:/app ml_analysis_image_api:latest
```
* (5) successful completion will result in a "results.txt" file in the current folder