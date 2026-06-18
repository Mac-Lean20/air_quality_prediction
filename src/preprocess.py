import pandas as pd
import sys
import os

_BASE = os.path.dirname(os.path.abspath(__file__))


def load_and_prepare_data(path):
    df = pd.read_csv(path, skiprows=1)
    df["time"] = pd.to_datetime(df["time"])
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month
    df["day"] = df["time"].dt.day
    df["hour"] = df["time"].dt.hour
    df = df.dropna()
    return df


if __name__ == "__main__":
    input_path = os.path.join(_BASE, "..", "data", "raw", "tera_analytics_data.csv")
    output_path = os.path.join(_BASE, "..", "data", "processed", "clean_data.csv")
    df = load_and_prepare_data(input_path)
    df.to_csv(output_path, index=False)
    print(f"Données nettoyées sauvegardées dans {output_path}")
