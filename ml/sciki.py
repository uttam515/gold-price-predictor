import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


# ── DATA LOADING ──────────────────────────────────────────────────────
df_gold = pd.read_csv("gold_prices_INR_2000_2026.csv")
df_us   = pd.read_csv("us_dollar.csv")

# ── FEATURES & LABEL ─────────────────────────────────────────────────
year     = df_gold[["Year"]].values.reshape(-1, 1)
us_price = df_us[["USD_to_INR"]].values.reshape(-1, 1)
prices   = df_gold[["Price_INR_per_10g"]].values.reshape(-1, 1)

X = np.hstack([year, us_price])
y = prices

# ── SCALING ───────────────────────────────────────────────────────────
scaler_X = RobustScaler()
scaler_y = RobustScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# ── TRAIN / TEST SPLIT ────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=67
)

# ── TRAIN ─────────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── PREDICT & INVERSE TRANSFORM ───────────────────────────────────────
y_pred_scaled = model.predict(X_test)
y_pred_actual = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1))
y_test_actual = scaler_y.inverse_transform(y_test)

# ── METRICS ───────────────────────────────────────────────────────────
mae = mean_absolute_error(y_test_actual, y_pred_actual)
r2  = r2_score(y_test_actual, y_pred_actual)
print(f"MAE : ₹{mae:,.2f}")
print(f"R²  : {r2:.4f}")

# ── PLOT ──────────────────────────────────────────────────────────────
# recover test years for a meaningful x-axis
X_test_original = scaler_X.inverse_transform(X_test)
test_years = X_test_original[:, 0].astype(int)
sort_idx   = np.argsort(test_years)          # sort so lines don't zigzag

plt.figure(figsize=(10, 5))
plt.plot(test_years[sort_idx], y_test_actual[sort_idx],
         label="Actual price", marker="o", markersize=5)
plt.plot(test_years[sort_idx], y_pred_actual[sort_idx],
         label="Predicted price", marker="x", markersize=5, linestyle="--")
plt.title("Gold price — actual vs predicted")
plt.xlabel("Year")
plt.ylabel("Price (INR per 10g)")
plt.xticks(test_years[sort_idx])
plt.legend()
plt.tight_layout()
plt.savefig("prediction_plot.png")
plt.show()

import joblib

joblib.dump(model, "gold_model.pkl")
joblib.dump(scaler_X, "scaler_X.pkl")
joblib.dump(scaler_y, "scaler_y.pkl")

print("Model saved successfully")







