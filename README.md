# Prédiction de la Qualité de l'Air (PM2.5)

Ce projet utilise un modèle **Random Forest** pour prédire les concentrations de **PM2.5** à partir de mesures de capteurs (PM1, coordonnées GPS, date/heure).

## Objectif

Exploiter 1,8 million de mesures de qualité de l'air collectées par des capteurs à Madagascar (31 mars 2024 → 5 juin 2026) pour construire un modèle capable de prédire les particules fines PM2.5.

## Variables

| Variable | Description |
|----------|-------------|
| `pm1` | Particules fines ≤ 1µm (entrée) |
| `pm25` | Particules fines ≤ 2.5µm (cible) |
| `latitude`, `longitude` | Position du capteur |
| `year`, `month`, `day`, `hour` | Extraites de la date |

## Performance

| Métrique | Valeur |
|----------|--------|
| MAE | 0.29 µg/m³ |
| RMSE | 1.15 µg/m³ |
| R² | 0.9984 |

Le R² de 0.9984 s'explique par la forte corrélation physique entre PM1 et PM2.5.

## Structure

```
├── data/raw/          # Données CSV brutes (ignorées par Git)
├── data/processed/    # Données nettoyées (ignorées par Git)
├── models/            # Modèle entraîné (.pkl)
├── notebooks/         # Notebook Jupyter d'exploration
├── src/               # Code source
│   ├── preprocess.py  # Nettoyage et préparation
│   ├── train.py       # Entraînement du modèle
│   ├── evaluate.py    # Évaluation et métriques
│   └── predict.py     # Prédiction interactive
├── results/           # Métriques et prédictions
├── requirements.txt   # Dépendances
└── README.md
```

## Utilisation

```bash
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
python src/predict.py
```
