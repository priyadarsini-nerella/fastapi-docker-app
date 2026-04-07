# app.py
from fastapi import FastAPI, Body
import pickle
import joblib


app = FastAPI()

# Load model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "California House Price Prediction API is running in docker!"}

@app.post("/predict")
def predict(features: list[float]= Body(
    ...,
    example=[8.3252, 41, 6.984, 1.023, 322, 2.555, 37.88, -122.23]
)):
    prediction = model.predict([features])
    return {"predicted_price": float(prediction[0])}
#python -m uvicorn app:app --reload
