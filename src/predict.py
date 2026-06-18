import sys
import os

_BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _BASE)

import joblib
import pandas as pd

model_path = os.path.join(_BASE, "..", "models", "random_forest_pm25.pkl")
model = joblib.load(model_path)

year = int(input("Année (ex: 2026) : "))
month = int(input("Mois (1-12) : "))
day = int(input("Jour (1-31) : "))
hour = int(input("Heure (0-23) : "))
pm1 = float(input("PM1 mesuré par le capteur : "))

sample = pd.DataFrame({
    "pm1": [pm1],
    "latitude": [-21.45],
    "longitude": [47.10],
    "year": [year],
    "month": [month],
    "day": [day],
    "hour": [hour]
})

prediction = model.predict(sample)
print(f"\nDate : {year}-{month:02d}-{day:02d} {hour:02d}h")
print(f"PM1 saisi    : {pm1}")
print(f"PM2.5 prédit : {prediction[0]:.2f}")
