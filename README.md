## ML Deployment Example with FastAPI

This project demonstrates **how to deploy a machine learning model** using **FastAPI**.  
The goal is to provide a simple, practical example for learning or demonstrating to future employers.

FastAPI documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

---

### Features

- Load a pre-trained ML model (`model.keras`) with its scaler and feature list.
- Provide an API endpoint to make predictions.
- Example dataset: Wisconsin Breast Cancer (all 30 features).
- Fully containerizable using Docker.

---


---

### Usage

#### 1. Run locally

1. Create a virtual environment:

```bash
python -m venv env
source env/bin/activate   # Linux/macOS
env\Scripts\activate      # Windows
```

2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Launch the FastAPI Server

```bash
uvicorn app.main:app --reload
```

4. Open your browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```

This provides the interactive Swagger UI to test the API endpoints.

#### 2. Run with Docker

1. Build the Docker image

```bash
docker build -t ml-fastapi-app .
```

```bash
2. Run the container

docker run -p 8000:8000 ml-fastapi-app
```

4. Open your browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```

#### Notes

The app loads the ML model, scaler, and feature list from app/model/.

All paths are centralized in app/config.py for consistent access across local, Docker, and CI/CD environments.

Tests are located under app/tests/ and can be run with:

  pytest app/tests

