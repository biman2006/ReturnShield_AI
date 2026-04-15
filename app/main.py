from fastapi import FastAPI 
from app.schemas import UserInput
from app.services.predictor import predict_fraud 

app=FastAPI()

@app.get("/")
def home():
    return {"message":"ReturnShield AI running"}

@app.post("/predict")
def predict(data:UserInput):
    result=predict_fraud(data) 
    return result 