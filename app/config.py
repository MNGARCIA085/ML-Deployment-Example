import os

# Base folder of the app package
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Model, scaler, features paths
MODEL_PATH = os.path.join(APP_DIR, "model", "model.keras")
SCALER_PATH = os.path.join(APP_DIR, "model", "scaler.pkl")
FEATURES_PATH = os.path.join(APP_DIR, "model", "features.json")
