from fastapi import FastAPI
from routers import predict

app = FastAPI(title="Prediction API")

app.include_router(predict.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Prediction API"}



# ....app$ uvicorn main:app --reload
