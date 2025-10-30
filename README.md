# DSA_210_Repository
#  The Relationship Between Movie Budgets, IMDB Ratings, and Revenue

##  Motivation
The film industry often assumes that higher-budget movies perform better both critically and financially.  
However, not every expensive movie achieves high ratings or commercial success.  
This project aims to explore **the impact of movie budgets on IMDB ratings and box office revenues.**  
By understanding these relationships, we can gain insights into whether money truly buys success in cinema and what other factors might contribute to a film’s outcome.

---

##  Objectives
- Investigate the correlation between **movie budgets** and **IMDB ratings**.  
- Analyze the relationship between **budgets** and **box office revenue**.  
- Identify whether specific **genres or production years** influence these relationships.  
- Evaluate if higher spending consistently leads to better critical or financial results.

---

## Data Sources
To conduct this analysis, data will be collected and merged from the following sources:

- **Primary Dataset:** [TMDB 5000 Movie Dataset (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
  Contains movie-level details such as `budget`, `revenue`, `vote_average`, `runtime`, `genres`, and `release_date`.  

- **Supplementary Dataset:** [IMDB Dataset](https://datasets.imdbws.com/)  
  Used to validate and enrich the data with additional rating information.

- **Optional Data:**  
  - Box Office Mojo or The Numbers for global revenue comparison  
  - Genre classification for cross-category analysis  

---

##  Data Analysis Plan

### 1. **Data Cleaning & Feature Engineering**
- Remove missing and duplicate records.  
- Convert `budget` and `revenue` into numeric format and standardize currency.  
- Create new features:  
  - `profit = revenue - budget`  
  - `return_ratio = revenue / budget`  

### 2. **Exploratory Visualizations**
- Distribution of budgets, revenues, and IMDB ratings  
- Scatter plots:  
  - `budget` vs `revenue`  
  - `budget` vs `vote_average`  
- Boxplots by genre to compare how budget relates to ratings  
- Correlation heatmap for numerical variables  

### 3. **Statistical Testing**
- **Pearson correlation tests** to quantify relationships:  
  - `budget` ↔ `revenue`  
  - `budget` ↔ `vote_average`  
- **Hypothesis Testing:**  
  - **H₀:** There is no significant relationship between movie budget and IMDB rating/revenue.  
  - **H₁:** Higher movie budgets are significantly associated with higher IMDB ratings and/or revenues.

### 4. **Modeling (Optional)**
- **Linear regression** to predict revenue based on budget and rating.  
- **Multiple regression** including genre and runtime as predictors.  

---

##  Expected Outcomes
By the end of this study, the project aims to answer the following questions:
- Do higher budgets lead to better IMDB ratings?  
- Are expensive movies guaranteed to earn higher box office revenue?  
- Which genres demonstrate the strongest link between investment and success?  
- Can we predict a film’s potential revenue from its budget and genre?

---

##  Limitations & Future Work
- The project relies on publicly available datasets, which may lack complete budget or revenue data.  
- Inflation and currency differences across years are not initially adjusted.  
- Future work could include sentiment analysis of reviews or adding cast/crew influence metrics.  

---

##  Conclusion
This project will provide valuable insights into how financial investment impacts both **critical reception (IMDB ratings)** and **financial performance (revenue)** of films.  
By identifying patterns in budget allocation and audience response, the study will help understand what truly defines a successful movie — **money, quality, or both.**

---

##  Timeline
| Date | Task |
|------|------|
| **31 Oct** | Submit project proposal on GitHub (this README file) |
| **28 Nov** | Complete data collection and exploratory analysis |
| **02 Jan** | Apply ML/regression models |
| **09 Jan** | Submit final report and presentation |

---

