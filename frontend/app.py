import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load("rf_model.pkl")

st.set_page_config(page_title="ReturnGuard AI", layout="centered")

st.title("🛡️ ReturnShield AI")
st.markdown("Detect suspicious e-commerce returns using AI")

st.divider()

# INPUTS
total_orders = st.number_input("Total Orders", min_value=1, value=10)
total_returns = st.number_input("Total Returns", min_value=0, value=1)
order_value = st.number_input("Order Value", min_value=0.0, value=1000.0)

account_age_days = st.number_input("Account Age (days)", min_value=1, value=100)
day_since_last_return = st.number_input("Days Since Last Return", min_value=0, value=10)
return_last_7_days = st.number_input("Returns in Last 7 Days", min_value=0, value=0)

product_category = st.selectbox(
    "Product Category",
    ["electronics", "fashion", "home", "beauty_&_self_care", "fitness_&_sports", "toys_&_kids"]
)

return_reason = st.selectbox(
    "Return Reason",
    ["damaged", "not_needed", "wrong_item", "size_issue"]
)

# BUTTON
if st.button("Check Fraud Risk 🚀"):
    
    # feature engineering
    return_ratio = total_returns / total_orders
    is_high_value = 1 if order_value > 3500 else 0

    data = pd.DataFrame([{
        "total_orders": total_orders,
        "total_returns": total_returns,
        "return_ratio": return_ratio,
        "order_value": order_value,
        "acc_age_days": account_age_days,
        "days_since_last_return": day_since_last_return,
        "return_last_7_days": return_last_7_days,
        "product_category": product_category,
        "return_reason": return_reason,
        "is_high_value": is_high_value
    }])

    prob = model.predict_proba(data)[0][1]

    # risk logic
    if prob > 0.6:
        risk = "🚨 High Risk"
        st.error(f"{risk} | Probability: {prob:.2f}")
    elif prob > 0.3:
        risk = "⚠️ Medium Risk"
        st.warning(f"{risk} | Probability: {prob:.2f}")
    else:
        risk = "✅ Low Risk"
        st.success(f"{risk} | Probability: {prob:.2f}")