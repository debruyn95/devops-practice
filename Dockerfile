# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install psutil

# Run the script
CMD ["python", "monitor.py"]