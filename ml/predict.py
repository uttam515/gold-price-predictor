import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "gold_model.pkl"))
scaler_X = joblib.load(os.path.join(BASE_DIR, "scaler_X.pkl"))
scaler_y = joblib.load(os.path.join(BASE_DIR, "scaler_y.pkl"))

def predict_gold_price(year, usd_to_inr):
    X = np.array([[year, usd_to_inr]])
    X_scaled = scaler_X.transform(X)
    y_scaled = model.predict(X_scaled)
    y_actual = scaler_y.inverse_transform(y_scaled.reshape(-1, 1))
    return float(y_actual[0][0])