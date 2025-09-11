# Import des librairies
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Chargement du dataset
data = pd.read_csv("enedis_dpe_merged1.csv", sep=";", encoding="utf-8")

# Affichage des premières lignes pour vérifier les colonnes
print("Colonnes disponibles : ", data.columns)
print(data.head())

# ===== Paramètres à définir à la main =====
target_col = "Consommation annuelle moyenne par logement de l'adresse (MWh)"  # colonne cible (y)
feature_col = "dpe_elec_ef_kwh_m2"  # colonne explicative (x) à changer manuellement
# ==========================================

# Vérification si les colonnes existent
if target_col not in data.columns or feature_col not in data.columns:
    raise ValueError(f"Assure-toi que {target_col} et {feature_col} sont bien dans le dataset")

# Suppression des lignes avec valeurs manquantes pour ces colonnes
data = data[[feature_col, target_col]].dropna()

# Séparation des variables
X = data[[feature_col]]  # variable explicative
y = data[target_col]      # variable cible

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Prédictions
y_pred = model.predict(X)

# Affichage des coefficients
print("Coefficient (pente) :", model.coef_[0])
print("Intercept :", model.intercept_)
print("R² :", r2_score(y, y_pred))
print("MSE :", mean_squared_error(y, y_pred))

# Tracé du nuage de points + droite de régression
plt.scatter(X, y, color='blue', label="Données réelles")
plt.plot(X, y_pred, color='red', linewidth=2, label="Droite de régression")
plt.xlabel(feature_col)
plt.ylabel(target_col)
plt.title(f"Régression linéaire: {target_col} vs {feature_col}")
plt.legend()
plt.savefig("char_reglin4.png")
