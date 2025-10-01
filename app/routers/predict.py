from fastapi import APIRouter
import pickle
import numpy as np
import pandas as pd
import json
from app.schemas import CancerInput
import tensorflow as tf
from app.config import MODEL_PATH, SCALER_PATH, FEATURES_PATH


router = APIRouter()





model = tf.keras.models.load_model(MODEL_PATH)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# Load feature names from JSON
with open(FEATURES_PATH, "r") as f:
    features = json.load(f)  # should be a list of 30 feature names



@router.post("/predict")
def predict(data: CancerInput):

    # Convert Pydantic model (CancerInput) to dict
    data_dict = data.dict()   # If using FastAPI Pydantic input

    # Map API-friendly names to model-friendly names
    rename_map = {
        "concave_points_mean": "concave points_mean",
        "concave_points_se": "concave points_se",
        "concave_points_worst": "concave points_worst"
    }

    # Apply renaming
    for k_api, k_model in rename_map.items():
        data_dict[k_model] = data_dict.pop(k_api)


    # Make sure the order of columns matches features.json
    X_df = pd.DataFrame([[data_dict[feat] for feat in features["features"]]],
                        columns=features["features"])

    # Scale
    X_scaled = scaler.transform(X_df)

    # Predict
    prediction = model.predict(X_scaled)

    pred_value = prediction[0][0]  # or prediction.item()
    prob = float(f"{pred_value:.3e}")  # scientific notation, float
    
    return {
        "probability": prob,
    }

 

"""
Encoder:
{"M": 1, "B": 0}
"""