import sys
import os

_BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _BASE)

import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from preprocess import load_and_prepare_data

df = load_and_prepare_data(
    os.path.join(_BASE, "..", "data", "raw", "tera_analytics_data.csv")
)

df = df.sample(n=100000, random_state=42)

feature_cols = ["pm1", "latitude", "longitude", "year", "month", "day", "hour"]
X = df[feature_cols]
y = df["pm25"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100, max_depth=10, random_state=42, n_jobs=1
)
model.fit(X_train, y_train)

model_path = os.path.join(_BASE, "..", "models", "random_forest_pm25.pkl")
joblib.dump(model, model_path)
print("Modèle sauvegardé.")
