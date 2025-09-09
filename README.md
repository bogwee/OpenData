# 📝 Plan de travail — DPE & Consommations électriques

## 1. Introduction & Contexte
- **Accroche** : *“On dit souvent que le DPE indique la performance énergétique d’un logement. Mais reflète-t-il vraiment la réalité des consommations électriques ?”*  
- **Problématique clé** :  
👉 *Dans quelle mesure les classes du Diagnostic de Performance Énergétique (DPE) reflètent-elles les consommations électriques réelles des logements, et quels gains peut-on attendre d’un changement de classe ?*  

- **Annonce du plan** :  
  1. Observer le lien entre DPE et consommations réelles.  
  2. Identifier les écarts et expliquer les causes.  
  3. Mesurer l’impact potentiel des rénovations.  
  4. Construire un outil d’aide à la décision.

---

## 2. Analyse des données & Sous-problématiques

### A. Fiabilité du DPE comme indicateur
- **Question** : *Le DPE est-il un bon prédicteur des consommations électriques réelles ?*  
- **Analyses** : comparaison consommation mesurée (Enedis) vs consommation conventionnelle (DPE).  
- **Outils** : corrélations, écarts moyens, distribution des erreurs.

---

### B. Variabilité liée aux comportements
- **Question** : *Pourquoi deux logements avec le même DPE peuvent-ils avoir des consommations réelles très différentes ?*  
- **Facteurs** : nombre d’occupants, habitudes de chauffage, équipements électroménagers, localisation géographique.  
- **Méthodes** : analyse de la dispersion (écart-type, boxplots), mise en évidence de cas atypiques.

---

### C. Impact d’un changement de classe DPE
- **Question** : *Combien peut-on économiser concrètement (en kWh et en €) en améliorant sa classe de DPE ?*  
- **Méthodes** : estimer les gains moyens de F → E, E → D, etc. ; traduire en économies financières selon un tarif de référence (€/kWh).  
- **Résultat attendu** : tableau clair des économies potentielles par transition de classe.

---

### D. Effet des caractéristiques du logement
- **Question** : *Quels paramètres (année de construction, isolation, mode de chauffage) expliquent le plus les différences de consommation ?*  
- **Analyses possibles** : régressions, arbres de décision ou importance des variables dans un modèle prédictif.  
- **Intérêt** : montrer que le DPE seul ne suffit pas → d’autres facteurs structurants doivent être pris en compte.

---

## 3. Discussion & Perspectives
- **Constats** :  
  - Limite du DPE (outil standardisé vs réalité vécue).  
  - Comportements et caractéristiques techniques tout aussi déterminants.  
- **Perspectives** :  
  - Enjeux politiques et sociaux (interdiction progressive des passoires thermiques).  
  - Impact économique des rénovations.

---

## 4. Application finale (logiciel prototype)

### **Nom : DPE-Réalité**
Un outil simple d’**aide à la décision** (développé par ex. en Python/Streamlit ou R/Shiny).

- **Fonctionnalités principales** :  
  1. **Entrée utilisateur** : classe DPE actuelle, surface, type de chauffage, année de construction, nombre d’occupants.  
  2. **Sortie** :  
     - Consommation électrique estimée par le DPE (valeur conventionnelle).  
     - Consommation réelle moyenne observée (issue des données Enedis).  
     - Écart probable (+/- écart-type).  
     - Économies potentielles (kWh et €) en cas d’amélioration de 1 ou 2 classes.  
  3. **Visualisation interactive** :  
     - Graphiques comparant DPE vs réalité.  
     - Distribution des écarts.  
     - Scénarios de rénovation.  

- **Impact attendu** :  
  - Un outil qui rend les données **parlantes et utiles**.  
  - Aide pratique pour locataires, propriétaires et décideurs publics.  

---

## 5. Résumé pour l’oral
- **Problématique accrocheuse** : le DPE reflète-t-il la réalité ?  
- **Sous-problématiques dynamiques** : fiabilité, variabilité, gains réels, facteurs explicatifs.  
- **Application concrète** : un outil interactif (DPE-Réalité) qui montre l’utilité directe de l’analyse.
