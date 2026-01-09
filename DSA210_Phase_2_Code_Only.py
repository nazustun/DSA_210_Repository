
# -*- coding: utf-8 -*-
"""
DSA210 – Phase 2: Statistical Analysis and Hypothesis Testing
Movie Budgets, Ratings, and Revenue

This script contains ONLY executable Python code (no markdown),
formatted to be uploaded directly to GitHub as a .py file,
similar to Kaan's Phase 2 structure.
"""

# ===============================
# Import Required Libraries
# ===============================
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, spearmanr, f_oneway

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
# Feature Engineering
# ===============================
tmdb["profit"] = tmdb["revenue"] - tmdb["budget"]
tmdb["roi"] = tmdb["revenue"] / tmdb["budget"]

tmdb["log_budget"] = np.log10(tmdb["budget"])
tmdb["log_revenue"] = np.log10(tmdb["revenue"])

def extract_main_genre(x):
    try:
        g = ast.literal_eval(x)
        return g[0]["name"] if g else "Unknown"
    except:
        return "Unknown"

tmdb["main_genre"] = tmdb["genres"].apply(extract_main_genre)

# ===============================
# Exploratory Data Analysis
# ===============================
plt.figure(figsize=(7,6))
sns.scatterplot(data=tmdb, x="log_budget", y="log_revenue", alpha=0.4)
plt.title("Budget vs Revenue (log-log)")
plt.show()

plt.figure(figsize=(7,6))
sns.scatterplot(data=tmdb, x="log_budget", y="vote_average", alpha=0.4)
plt.title("Budget vs Rating")
plt.show()

# ===============================
# Correlation Analysis
# ===============================
num_cols = [
    "budget","revenue","vote_average","runtime",
    "profit","roi","log_budget","log_revenue","release_year"
]

corr = tmdb[num_cols].corr(numeric_only=True)

plt.figure(figsize=(10,7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="viridis")
plt.title("Correlation Heatmap")
plt.show()

# ===============================
# Genre-Based Analysis
# ===============================
top_genres = tmdb["main_genre"].value_counts().head(10).index
subset = tmdb[tmdb["main_genre"].isin(top_genres)]

plt.figure(figsize=(12,6))
sns.boxplot(data=subset, x="main_genre", y="roi")
plt.xticks(rotation=45)
plt.title("ROI by Genre (Top 10)")
plt.show()

# ===============================
# Time-Based Analysis
# ===============================
tmdb["decade"] = (tmdb["release_year"] // 10 * 10).astype(int)

decade_stats = tmdb.groupby("decade")["roi"].median().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=decade_stats, x="decade", y="roi", marker="o")
plt.title("Median ROI by Decade")
plt.show()

# ===============================
# Hypothesis Testing
# ===============================
# H1: Budget vs Revenue
r1, p1 = pearsonr(tmdb["budget"], tmdb["revenue"])
r1s, p1s = spearmanr(tmdb["budget"], tmdb["revenue"])

print("H1 Pearson:", r1, "p:", p1)
print("H1 Spearman:", r1s, "p:", p1s)

# H2: Budget vs Rating
r2, p2 = pearsonr(tmdb["budget"], tmdb["vote_average"])
r2s, p2s = spearmanr(tmdb["budget"], tmdb["vote_average"])

print("H2 Pearson:", r2, "p:", p2)
print("H2 Spearman:", r2s, "p:", p2s)

# H3: Genre differences (ANOVA)
anova_groups = [subset.loc[subset["main_genre"] == g, "roi"] for g in top_genres]
F, p = f_oneway(*anova_groups)

print("H3 ANOVA F:", F, "p:", p)

# H4: Decade differences (ANOVA)
top_decades = tmdb["decade"].value_counts().head(8).index
anova_dec = [tmdb.loc[tmdb["decade"] == d, "roi"] for d in top_decades]
F2, p2 = f_oneway(*anova_dec)

print("H4 ANOVA F:", F2, "p:", p2)
