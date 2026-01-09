
# -*- coding: utf-8 -*-
"""
DSA210 – Phase 3: Machine Learning Methods (Code Only)
Movie Budgets, Ratings, and Revenue

This script contains ONLY executable Python code (no markdown),
formatted to be uploaded directly to GitHub as a .py file,
similar to Kaan's Phase 3 structure.

Goals:
- Regression: predict log(revenue)
- Classification: predict Hit vs Flop
- Pipelines: preprocessing + models
- Baseline model comparison + evaluation on test set
"""

# ===============================
# Import Required Libraries
# ===============================
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

from sklearn.metrics import (
    r2_score, root_mean_squared_error,
    accuracy_score, f1_score, roc_auc_score,
    ConfusionMatrixDisplay, RocCurveDisplay
)

plt.style.use("default")
sns.set(style="whitegrid")

# ===============================
# Load Dataset
# ===============================
tmdb = pd.read_csv("tmdb_5000_movies.csv")

# ===============================
# Data Cleaning & Alignment
# ===============================
tmdb["budget"] = pd.to_numeric(tmdb["budget"], errors="coerce")
tmdb["revenue"] = pd.to_numeric(tmdb["revenue"], errors="coerce")
tmdb["vote_average"] = pd.to_numeric(tmdb["vote_average"], errors="coerce")
tmdb["runtime"] = pd.to_numeric(tmdb["runtime"], errors="coerce")
tmdb["release_year"] = pd.to_numeric(tmdb["release_date"].astype(str).str[:4], errors="coerce")

tmdb = tmdb.dropna(subset=["budget","revenue","vote_average","runtime","release_year"])
tmdb = tmdb[(tmdb["budget"] > 0) & (tmdb["revenue"] > 0)]

# ===============================
# Digital Feature Engineering
# ===============================
tmdb["log_budget"] = np.log10(tmdb["budget"])
tmdb["log_revenue"] = np.log10(tmdb["revenue"])

def extract_main_genre(x):
    try:
        g = ast.literal_eval(x)
        return g[0]["name"] if g else "Unknown"
    except:
        return "Unknown"

tmdb["main_genre"] = tmdb["genres"].apply(extract_main_genre)

# Feature lists
features_num = ["log_budget", "vote_average", "runtime"]
features_cat = ["main_genre"]

# ===============================
# Preprocessing Pipeline
# ===============================
preprocess = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), features_num),
        ("cat", OneHotEncoder(handle_unknown="ignore"), features_cat)
    ]
)

# ===============================
# Train–Test Split (Regression)
# ===============================
X_reg = tmdb[features_num + features_cat]
y_reg = tmdb["log_revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# ===============================
# Baseline Model Comparison (Regression)
# ===============================
models_reg = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.01),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=300, random_state=42)
}

reg_results = []

for name, model in models_reg.items():
    pipe = Pipeline([("prep", preprocess), ("model", model)])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    reg_results.append({
        "Model": name,
        "R2": r2_score(y_test, preds),
        "RMSE": root_mean_squared_error(y_test, preds)
    })

reg_results_df = pd.DataFrame(reg_results).sort_values("R2", ascending=False)
print("\n=== Regression Results (Test Set) ===")
print(reg_results_df)

# Predicted vs Actual plot for best regression model
best_reg_name = reg_results_df.iloc[0]["Model"]
best_reg_model = models_reg[best_reg_name]

best_reg_pipe = Pipeline([("prep", preprocess), ("model", best_reg_model)])
best_reg_pipe.fit(X_train, y_train)
best_pred = best_reg_pipe.predict(X_test)

plt.figure(figsize=(7,6))
plt.scatter(y_test, best_pred, alpha=0.5)
mn = min(y_test.min(), best_pred.min())
mx = max(y_test.max(), best_pred.max())
plt.plot([mn, mx], [mn, mx], "r--")
plt.xlabel("Actual log(Revenue)")
plt.ylabel("Predicted log(Revenue)")
plt.title(f"Regression (Test): Actual vs Predicted – {best_reg_name}")
plt.show()

# ===============================
# Train–Test Split (Classification)
# ===============================
# Define Hit vs Flop using top 25% revenue threshold
threshold = tmdb["revenue"].quantile(0.75)
tmdb["is_hit"] = (tmdb["revenue"] >= threshold).astype(int)

X_clf = tmdb[features_num + features_cat]
y_clf = tmdb["is_hit"]

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# ===============================
# Baseline Model Comparison (Classification)
# ===============================
models_clf = {
    "Logistic Regression": LogisticRegression(max_iter=2000),
    "Random Forest Classifier": RandomForestClassifier(n_estimators=300, random_state=42)
}

clf_results = []

for name, model in models_clf.items():
    pipe = Pipeline([("prep", preprocess), ("model", model)])
    pipe.fit(X_train_c, y_train_c)

    preds = pipe.predict(X_test_c)
    probas = pipe.predict_proba(X_test_c)[:,1]

    clf_results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test_c, preds),
        "F1": f1_score(y_test_c, preds),
        "ROC_AUC": roc_auc_score(y_test_c, probas)
    })

clf_results_df = pd.DataFrame(clf_results).sort_values("ROC_AUC", ascending=False)
print("\n=== Classification Results (Test Set) ===")
print(clf_results_df)

# ===============================
# Model Evaluation on Test Data (Best Classifier)
# ===============================
best_clf_name = clf_results_df.iloc[0]["Model"]
best_clf_model = models_clf[best_clf_name]

best_clf_pipe = Pipeline([("prep", preprocess), ("model", best_clf_model)])
best_clf_pipe.fit(X_train_c, y_train_c)

best_preds = best_clf_pipe.predict(X_test_c)
best_probas = best_clf_pipe.predict_proba(X_test_c)[:,1]

ConfusionMatrixDisplay.from_predictions(y_test_c, best_preds)
plt.title(f"Confusion Matrix (Test) – {best_clf_name}")
plt.show()

RocCurveDisplay.from_predictions(y_test_c, best_probas)
plt.title(f"ROC Curve (Test) – {best_clf_name}")
plt.show()
