FROM python:latest

# Install required packages
RUN pip install pandas scikit-learn

# Set the working directory
WORKDIR /app

# Copy the Python script into the image
COPY script.py /app

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "/app/script.py"]