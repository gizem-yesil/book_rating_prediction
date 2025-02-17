from fastapi.testclient import TestClient
from main import app  


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working!"} 

def test_predict_valid_input():
    response = client.post("/predict", json={"text": "This is a great book!"})
    assert response.status_code == 200
    assert "predicted_rating" in response.json()  

def test_predict_invalid_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422  

def test_predict_non_string_input():
    response = client.post("/predict", json={"text": 12345})
    assert response.status_code == 422 
