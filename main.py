# app.py
from fastapi import FastAPI
import pickle
import joblib


app = FastAPI()

# Load model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "California House Price Prediction API is running in docker!"}

@app.post("/predict")
def predict(features: list[float]):
    prediction = model.predict([features])
    return {"predicted_price": float(prediction[0])}
#python -m uvicorn app:app --reload