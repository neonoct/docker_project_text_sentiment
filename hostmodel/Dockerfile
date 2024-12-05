# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and scripts
COPY requirements.txt .
COPY app.py .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

# Expose port for the app
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
