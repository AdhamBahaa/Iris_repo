# FROM python:3.6-jessie

# LABEL maintainer="https://github.com/AchilleasKn"

# RUN pip3 install --upgrade pip
# # RUN apt-get update
# # RUN apt-get -y install python3-pip

# # copy all files of the current directory to the folder /app
# COPY . /app
# WORKDIR /app

# # install requiremtnts
# RUN pip3 install -r requirements.txt

# # run the flask API
# CMD python3 api.py

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=api.py

# Run the application
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", " & " , "streamlit run iris_frontend_streamlit.py"]
CMD ["/bin/sh", "-c", "flask run --host=0.0.0.0 --port=5000 & streamlit run iris_frontend_streamlit.py"]