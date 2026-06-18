# Prédiction de la Qualité de l'Air (PM2.5)

Ce projet utilise un modèle **Random Forest** pour prédire les concentrations de **PM2.5** à partir de mesures de capteurs (PM1, coordonnées GPS, date/heure).

## Objectif

Exploiter 1,8 million de mesures de qualité de l'air collectées par des capteurs à Madagascar (31 mars 2024 → 5 juin 2026) pour construire un modèle capable de prédire les particules fines PM2.5.

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

## Prérequis

- **Fichier CSV** : Placer `tera_analytics_data.csv` dans `data/raw/` push . Contacter l'auteur pour l'obtenir.
- Python 3.10+

## Utilisation

```bash
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
python src/predict.py
```
