
# DSA210 – Final Project Report
## The Relationship Between Movie Budgets, Ratings, and Box Office Revenue

**Student:** Naz Üstün  
**Course:** DSA210 – Data Science Analysis
**Term:** Fall 2025–2026  

---

## 1. Introduction

The film industry frequently assumes that higher production budgets lead to greater commercial success and better audience reception. Large-scale productions often involve extensive marketing, advanced technology, and well-known cast members, all of which are expected to contribute positively to a movie’s performance. However, many high-budget films fail to meet expectations, while some low-budget films achieve remarkable success.

This project investigates the relationship between **movie budgets**, **audience ratings**, and **box office revenue** using data-driven methods. The aim is to determine whether financial investment alone explains movie success or whether other factors such as genre and release period contribute significantly.

---

## 2. Data Description

### 2.1 Dataset
The primary dataset used in this project is the **TMDB 5000 Movies Dataset**, which contains information on approximately 5,000 movies. Key variables include:
- Budget
- Revenue
- Vote average (ratings)
- Runtime
- Genres
- Release date

Only movies with valid, positive budget and revenue values were included in the analysis.

### 2.2 Data Preprocessing
Several preprocessing steps were applied:
- Conversion of budget and revenue to numeric format
- Removal of missing and invalid values
- Logarithmic transformation of budget and revenue to reduce skewness
- Feature engineering for profit, ROI, genre, and release decade

---

## 3. Research Questions and Hypotheses

### Research Questions
1. Is movie budget associated with box office revenue?
2. Is movie budget associated with audience ratings?
3. Do these relationships vary across genres?
4. Does movie success differ across release periods?

### Hypotheses
- **H1:** Movie budget is significantly related to box office revenue.
- **H2:** Movie budget is significantly related to audience ratings.
- **H3:** Genre moderates the relationship between budget and success.
- **H4:** Movie success differs across release periods.

---

## 4. Phase 2 – Exploratory Data Analysis and Statistical Testing

### 4.1 Exploratory Data Analysis
EDA revealed a strong positive relationship between budget and revenue, particularly after logarithmic transformation. In contrast, the relationship between budget and ratings appeared weak. Genre-based and time-based visualizations suggested heterogeneity in movie success.

### 4.2 Statistical Tests
- **Correlation analysis** showed a strong and statistically significant association between budget and revenue.
- The association between budget and ratings was weak and often statistically insignificant.
- **ANOVA tests** indicated significant differences in ROI across genres and release decades.

These findings support H1, partially support H3 and H4, and provide limited support for H2.

---

## 5. Phase 3 – Machine Learning Methods

### 5.1 Regression Analysis
Multiple regression models were trained to predict log-transformed revenue:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor

Random Forest achieved the highest predictive performance, indicating the presence of nonlinear relationships.

### 5.2 Classification Analysis
Movies were classified as **Hit** or **Flop** based on whether they belonged to the top 25% of revenue:
- Logistic Regression
- Random Forest Classifier

Random Forest outperformed Logistic Regression in terms of accuracy, F1-score, and ROC-AUC.

---

## 6. Results and Discussion

The results confirm that movie budget is a strong predictor of revenue but not of audience ratings. Genre and release period introduce additional variation that cannot be captured by budget alone. Machine learning models further demonstrate that nonlinear methods capture complex interactions more effectively than linear baselines.

---

## 7. Limitations and Future Work

This study relies on publicly available data, which may contain reporting inaccuracies. Inflation and regional revenue differences were not adjusted. Future work could incorporate:
- Inflation-adjusted budgets
- Cast and director popularity
- Sentiment analysis of reviews

---

## 8. Conclusion

This project demonstrates that while financial investment plays a major role in box office success, it is not sufficient to guarantee positive audience reception. By combining statistical analysis and machine learning, the study provides a comprehensive view of the factors influencing movie success.

---

## 9. Repository Structure

The complete project, including all phases and code, is available on GitHub:
- Phase 2: Statistical Analysis (Notebook + Python)
- Phase 3: Machine Learning Methods (Notebook + Python)
- Dataset: TMDB 5000 Movies

