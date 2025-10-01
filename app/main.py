from fastapi import FastAPI
from app.routers import predict

app = FastAPI(title="Prediction API")

app.include_router(predict.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Prediction API"}


# ......ML-Deployment-Example$ uvicorn app.main:app --reload

