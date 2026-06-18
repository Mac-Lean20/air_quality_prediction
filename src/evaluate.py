import sys
import os

_BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _BASE)

import joblib
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from preprocess import load_and_prepare_data

df = load_and_prepare_data(
    os.path.join(_BASE, "..", "data", "raw", "tera_analytics_data.csv")
)

feature_cols = ["pm1", "latitude", "longitude", "year", "month", "day", "hour"]
X = df[feature_cols]
y = df["pm25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_path = os.path.join(_BASE, "..", "models", "random_forest_pm25.pkl")
model = joblib.load(model_path)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("RMSE :", rmse)
print("R² :", r2)

metrics_path = os.path.join(_BASE, "..", "results", "metrics.txt")
with open(metrics_path, "w") as f:
    f.write(f"MAE : {mae}\n")
    f.write(f"RMSE : {rmse}\n")
    f.write(f"R2 : {r2}\n")
