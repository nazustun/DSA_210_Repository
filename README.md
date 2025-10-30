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

##  Data Sources

To conduct this analysis, multiple movie-related datasets will be used and merged to ensure accuracy, richness, and analytical depth. Each dataset was selected for a specific reason and contributes to the project in a unique way.

---

###  Primary Dataset: [TMDB 5000 Movie Dataset (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
**Reason for Selection:**  
This dataset provides a comprehensive collection of over 5000 movies, including detailed financial and audience-related variables such as `budget`, `revenue`, `vote_average`, `runtime`, `genres`, and `release_date`.  
It is one of the most widely used and clean movie datasets, making it ideal for analyzing relationships between budget, ratings, and profitability.

**How It Will Be Used:**  
- As the **main data source** for all statistical analyses and visualizations.  
- The variables `budget`, `revenue`, and `vote_average` will be used to calculate:
  - **Profit:** `revenue - budget`  
  - **Return on Investment (ROI):** `revenue / budget`  
- Genre and release date data will support segmentation analyses (e.g., comparing genres or release periods).

---

### Supplementary Dataset: [IMDB Dataset](https://datasets.imdbws.com/)
**Reason for Selection:**  
While the TMDB dataset includes its own `vote_average`, the IMDB dataset offers more **authoritative and consistent user ratings**, as well as additional metadata like the number of votes and title identifiers.  
Using IMDB data helps validate and strengthen the accuracy of the rating analysis.

**How It Will Be Used:**  
- To **cross-check and validate** movie ratings with TMDB data.  
- To include **extra variables** such as `num_votes` and `IMDB_rating` for deeper correlation analysis.  
- Movies will be merged using title and release year as matching keys.

---

###  Optional Data: [Box Office Mojo](https://www.boxofficemojo.com/) or [The Numbers](https://www.the-numbers.com/)
**Reason for Selection:**  
TMDB data often lists incomplete or region-specific revenue values. Box Office Mojo and The Numbers provide **more accurate and global revenue statistics**, which can fill gaps and increase the reliability of the financial analysis.

**How It Will Be Used:**  
- To **enrich and verify** revenue data from TMDB, ensuring figures reflect total worldwide earnings.  
- To compare **regional vs. global revenue** where applicable.  
- May also be used to categorize films by **box office success levels** (e.g., “flop”, “hit”, “blockbuster”).

---

### 🎭 Genre Classification Data
**Reason for Selection:**  
Analyzing how budget and revenue relationships differ across genres adds interpretability to the results.  
For instance, action films might have high budgets and returns, whereas dramas could rely more on critical success.

**How It Will Be Used:**  
- To group movies by genre and **compare budget–rating–revenue patterns**.  
- To create **visualizations** that highlight which genres yield the best return or highest ratings.  
- To support potential **multi-variable regression models** that include genre as a categorical variable.

---


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

