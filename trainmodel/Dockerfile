# Use Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and the train script to the container
COPY requirements.txt .
COPY train.py .

# Upgrade pip and install Python dependencies
RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

# Run the training script
CMD ["python", "train.py"]
