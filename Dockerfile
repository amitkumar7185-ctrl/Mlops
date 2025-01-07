# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
