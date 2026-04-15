import joblib 
import pandas as pd 
from app.utils.feature_Engineering import create_features 

model=joblib.load("rf_model.pkl")

def predict_fraud(data):
    features=create_features(data) 

    df=pd.DataFrame([features])

    prob=model.predict_proba(df)[0][1] 

    if prob>0.7:
        risk="High Risk 🚨" 
    elif prob>0.4:
        risk="Medium Risk ⚠️"

    else:
        risk="Low Risk ✅"

    return {
        "fraud_probability": round(prob,2),
        "risk_level": risk
    }