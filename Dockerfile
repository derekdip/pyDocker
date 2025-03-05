# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /workspace

# Install Git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs

RUN apt-get update && apt-get install -y npm


EXPOSE 3000 8000
# Optionally, install any dependencies (if you have a requirements.txt)
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# By leaving the CMD blank, we'll let the user specify what file to run
CMD ["python"]
