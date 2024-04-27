# Use the official Python image as base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["streamlit", "run", "dashboard.py"]
