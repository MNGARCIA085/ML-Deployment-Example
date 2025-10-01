# test_predict.py
from fastapi.testclient import TestClient
from main import app  # your FastAPI instance

client = TestClient(app)

# minimal valid input
sample_input = {
    "radius_mean": 10.0,
    "texture_mean": 15.0,
    "perimeter_mean": 70.0,
    "area_mean": 400.0,
    "smoothness_mean": 0.1,
    "compactness_mean": 0.2,
    "concavity_mean": 0.1,
    "concave_points_mean": 0.05,
    "symmetry_mean": 0.2,
    "fractal_dimension_mean": 0.06,
    "radius_se": 0.3,
    "texture_se": 1.2,
    "perimeter_se": 2.0,
    "area_se": 15.0,
    "smoothness_se": 0.005,
    "compactness_se": 0.02,
    "concavity_se": 0.01,
    "concave_points_se": 0.005,
    "symmetry_se": 0.02,
    "fractal_dimension_se": 0.003,
    "radius_worst": 12.0,
    "texture_worst": 18.0,
    "perimeter_worst": 80.0,
    "area_worst": 500.0,
    "smoothness_worst": 0.12,
    "compactness_worst": 0.25,
    "concavity_worst": 0.15,
    "concave_points_worst": 0.08,
    "symmetry_worst": 0.25,
    "fractal_dimension_worst": 0.07
}

def test_predict_status():
    response = client.post("/api/predict", json=sample_input)
    assert response.status_code == 200

def test_predict_response_keys():
    response = client.post("/api/predict", json=sample_input)
    data = response.json()
    assert "probability" in data


def test_predict_types():
    response = client.post("/api/predict", json=sample_input)
    data = response.json()
    assert isinstance(data["probability"], float)

