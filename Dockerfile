# Use official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app


# Expose the port Flask is running on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
