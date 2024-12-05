# Dockerized Sentiment Analysis API

This project demonstrates a **Dockerized Sentiment Analysis API** built using **Flask** and **Hugging Face's Transformers library**. The setup includes two Docker containers: one for training the model (`trainmodel`) and another for hosting the API (`hostmodel`).

## Features
- **Train Model**: Automatically downloads and initializes a pre-trained sentiment analysis model.
- **Host API**: Provides a `/predict` endpoint to analyze the sentiment of text.

---

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Docker
- Docker Compose

### Folder Structure
```
.
├── hostmodel
│   ├── app.py             # Flask app for serving predictions
│   ├── Dockerfile         # Dockerfile for hosting container
│   ├── requirements.txt   # Dependencies for the Flask app
├── trainmodel
│   ├── train.py           # Script for training/preparing the model
│   ├── Dockerfile         # Dockerfile for training container
│   ├── requirements.txt   # Dependencies for the training script
├── docker-compose.yml     # Defines and manages the two containers
```

---

## How to Use

### 1. Build and Start the Containers
Run the following commands to build the Docker images and start the containers:
```bash
docker-compose build
docker-compose up
```

### 2. Test the API
Once the containers are running, the API will be accessible at `http://localhost:5000`.

#### Example Request
You can test the `/predict` endpoint using `curl` or any API testing tool like Postman.

##### Using `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"I love this product!\"}" http://localhost:5000/predict
```

##### Example Response:
```json
{
    "predictions": [
        {
            "label": "POSITIVE",
            "score": 0.999
        }
    ]
}
```

---

## Technical Details

### Training Container (`trainmodel`)
- **Purpose**: Downloads and prepares the sentiment analysis model.
- **Key File**: `train.py`
- **Base Image**: Python 3.10 Slim
- **Command**: Runs `train.py` when the container starts.

### Hosting Container (`hostmodel`)
- **Purpose**: Hosts the Flask application to provide sentiment predictions.
- **Key File**: `app.py`
- **Base Image**: Python 3.10 Slim
- **Endpoint**: `/predict` (Accepts `POST` requests with `{"text": "your text"}`).

---

## Requirements
Dependencies for each container are listed in their respective `requirements.txt` files.

### Host Model Requirements (`hostmodel/requirements.txt`):
```
flask==2.1.1
transformers==4.31.0
```

### Train Model Requirements (`trainmodel/requirements.txt`):
```
transformers==4.31.0
```

---

## Notes
- The project uses **Hugging Face's Transformers** for sentiment analysis.
- This is a development setup. For production, consider using a production-ready WSGI server like `gunicorn` for hosting Flask apps.
- Do not terminate the docker-compose build if it takes much as it can take up to 5 minutes, this is because i used pip freeze for the requirements.txt so there maybe more than enough packages that are being installed.

---

## Troubleshooting

### Common Errors:
1. **404 Not Found**:
   - Ensure you're sending a `POST` request to `/predict`.
   - Use tools like `curl` or Postman to debug.

2. **Dependency Issues**:
   - Ensure `requirements.txt` is correct and compatible with the base Python image.

3. **Port Binding Issue**:
   - Verify no other application is using port 5000 on your system.

---

## Author
Ahmet Furkan Atal
Refined by ChatGPT-(Because why not :-) 

Feel free to extend or improve this project!

