<p align="center">
  <img src="assets/header.svg" alt="Patient Health Records Pipeline" width="100%">
</p>

<br>

<img src="assets/title_overview.svg" alt="Project Overview" width="100%">

<br>

This project constructs a comprehensive **Data Preprocessing, Missing Value Imputation & Outlier Handling pipeline** applied to a patient clinical records dataset. It covers diagnosing missingness patterns, comparing single-variable vs. advanced multivariate imputation strategies (Mean/Mode, Random Sample with indicators, KNN, and MICE), detecting outliers via multiple statistical methods (Z-score, IQR, and Percentiles), and repairing data quality through Winsorization and percentile clipping.

The implementation is fully coded and documented in Python within a Jupyter Notebook — **[pr_2.ipynb](file:///d:/RW/RW_Exam/Data_Preprocecing/PR_2/pr_2.ipynb)**.

<br>

---

<img src="assets/title_tools.svg" alt="Tools Used" width="100%">

<br>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/Jupyter-3F3F3F?style=for-the-badge&logo=jupyter&logoColor=F37626">
  <img src="https://img.shields.io/badge/Pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-%23013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/SciPy-%230C55A5?style=for-the-badge&logo=scipy&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white">
</p>

<br>

---

<img src="assets/title_parta.svg" alt="Part A — Handling Missing Values" width="100%">

<br>

### 🔍 Dataset Profile & Diagnosis
The source dataset — **[Patient_Health_Records_Dataset.csv](file:///d:/RW/RW_Exam/Data_Preprocecing/PR_2/Patient_Health_Records_Dataset.csv)** — contains 500 patient records across 9 clinical columns. High levels of missingness were diagnosed across multiple features:

| Column | Missing Count | Percentage | Imputation Strategy Used |
|---|---|---|---|
| `patient_id` | 0 | 0.0% | None (Unique Identifier) |
| `age` | 42 | 8.4% | Missing Indicator + Random Sample Imputation / KNN / MICE |
| `gender` | 22 | 4.4% | Most Frequent (Mode) Imputation |
| `region` | 23 | 4.6% | Most Frequent (Mode) Imputation |
| `bmi` | 47 | 9.4% | Mean Imputation / KNN / MICE |
| `blood_pressure` | 0 | 0.0% | None |
| `cholesterol` | 42 | 8.4% | KNN / MICE |
| `glucose` | 34 | 6.8% | KNN / MICE |
| `disease_risk` | 0 | 0.0% | None (Target Class Label) |

---

### 🛠 Imputation Implementations

#### 1. Simple Imputation (Numerical)
Mean imputation replaces missing cells with the column average. This is applied to `bmi` as a quick baseline:
```python
from sklearn.impute import SimpleImputer # L22 in notebook

mean_Imputer = SimpleImputer(strategy='mean')
data['bmi'] = mean_Imputer.fit_transform(data[['bmi']])
```

#### 2. Simple Imputation (Categorical)
Mode imputation replaces missing text labels with the most frequent value. This is applied to `region` and `gender`:
```python
most_frequent_Imputer = SimpleImputer(strategy='most_frequent')
data['region'] = most_frequent_Imputer.fit_transform(data[['region']]).flatten()
data['gender'] = most_frequent_Imputer.fit_transform(data[['gender']]).flatten()
```

#### 3. Missing Indicator + Random Sample Imputation
To preserve variance, a boolean flag indicates missingness, and random values are sampled from observed distributions to fill missing entries in `age`:
```python
# Create missing flag
data["age_missing"] = data["age"].isnull().astype(int)

# Random sampling
random_sample = data["age"].dropna().sample(
    data["age"].isnull().sum(),
    random_state=42,
    replace=True
)
data.loc[data["age"].isnull(), "age"] = random_sample.values
```

#### 4. KNN Imputer
Nearest-neighbor imputation estimates missing values using distance metrics from similar rows:
```python
from sklearn.impute import KNNImputer # L23 in notebook

cols = ["age", "bmi", "blood_pressure", "cholesterol", "glucose"]
knn = KNNImputer(n_neighbors=5)
data[cols] = knn.fit_transform(data[cols])
```

#### 5. MICE Algorithm (Multiple Imputation by Chained Equations)
MICE creates multiple individual imputations by running regression models sequentially across other feature predictors:
```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer # L25 in notebook

cols = ["age", "bmi", "blood_pressure", "cholesterol", "glucose"]
mice = IterativeImputer(random_state=42)
data[cols] = mice.fit_transform(data[cols])
```

> [!NOTE]
> Advanced multivariate imputations (like MICE) preserve the covariance structure between clinical columns much better than simple univariate measures.

<br>

---

<img src="assets/title_partb.svg" alt="Part B — Handling Outliers" width="100%">

<br>

Four outlier identification and processing methods were demonstrated to evaluate distribution distortion:

### 1. Z-Score Method
Identifies data points lying further than $\pm3$ standard deviations from the sample mean. Used to flag extreme values:
```python
from scipy.stats import zscore # L20 in notebook

data["z_score"] = zscore(data["blood_pressure"])
outliers = data[abs(data["z_score"]) > 3]
```

### 2. Interquartile Range (IQR) Method
Calculates IQR ($Q3 - Q1$) to establish a valid boundary $[Q1 - 1.5 \times IQR, \ Q3 + 1.5 \times IQR]$.
* Applied to `bmi`:
  * **$Q1$**: 21.8 · **$Q3$**: 30.9 · **IQR**: 9.1
  * **Boundaries**: $[8.15, \ 44.55]$
  * **Outliers Removed**: 8 rows
  * **Mean Shift**: 26.73 (Before) $\rightarrow$ 26.27 (After)

```python
Q1 = data["bmi"].quantile(0.25)
Q3 = data["bmi"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)
df_clean = data[(data["bmi"] >= lower_limit) & (data["bmi"] <= upper_limit)]
```

### 3. Percentile Method
Drops observations that fall in the extreme tails (under the 1st percentile or over the 99th percentile).
* Applied to `blood_pressure`:
  * **1st Percentile**: 91.48 · **99th Percentile**: 261.86
  * **Outliers Removed**: 10 rows
  * **Mean Shift**: 137.74 (Before) $\rightarrow$ 136.72 (After)

```python
lower_limit = data['blood_pressure'].quantile(0.01)
upper_limit = data['blood_pressure'].quantile(0.99)
df_clean = data[(data['blood_pressure'] >= lower_limit) & (data['blood_pressure'] <= upper_limit)]
```

### 4. Winsorization
Clips outliers instead of dropping rows. Values outside the 1st-99th percentile limits are replaced with the respective boundary thresholds, preserving the entire sample size.
* Applied to `blood_pressure`:
  * **Sample Size**: Maintained at 500 rows (no records deleted)
  * **Original Mean**: 137.74 · **Winsorized Mean**: 137.63

```python
from scipy.stats.mstats import winsorize # L26 in notebook

data["winsorized"] = winsorize(data['blood_pressure'], limits=[0.01, 0.01])
```

<br>

---

<img src="assets/title_partc.svg" alt="Part C — Final Cleaned Dataset" width="100%">

<br>

To prepare a single finalized data frame for prediction or downstream ML modeling:
1. Missing fields were imputed utilizing the multivariate [IterativeImputer](file:///d:/RW/RW_Exam/Data_Preprocecing/PR_2/pr_2.ipynb#L25) (MICE).
2. Outliers were capped across all clinical numeric features using a 1st to 99th percentile clipping range to preserve all 500 records:

```python
for col in ["bmi", "blood_pressure", "cholesterol", "glucose"]:
    data[col] = data[col].clip(
        lower=data[col].quantile(0.01),
        upper=data[col].quantile(0.99)
    )
```

The resulting clean dataset contains **0 missing values** and retains its original structural rows for complete analytical downstream readiness.

<br>

---

<img src="assets/title_results.svg" alt="Brief Report &amp; Insights" width="100%">

<br>

### ❓ Key Evaluation Questions

#### 1. Which imputation strategy was most effective?
* **Answer**: The **MICE (IterativeImputer)** algorithm proved most effective. Simple estimators like Mean and Median artificially shrink the variance and ignore inter-feature dynamics. MICE preserves dataset covariance by treating each attribute as a function of the others in round-robin regression steps.

#### 2. Which outlier handling method preserved data quality best?
* **Answer**: **Winsorization** (percentile capping) preserved quality best. While Z-Score and IQR methods flag outliers effectively, removing them drops sample sizes and causes data loss. Winsorization mitigates extreme deviations by capping values, keeping all observations intact.

#### 3. How did data cleaning improve dataset usability?
* **Answer**: It corrected systematic bias (imputing missing measurements like `bmi`, `glucose` and `cholesterol`) and normalized variance (capping outlier peaks). This establishes a mathematically sound, complete dataset ready for statistical analysis and machine learning.

<br>

---

### 👤 Priyansh Vekariya

*   📍 Ahmedabad, Gujarat, India
*   ⭐ If you found this data pipeline useful, give it a star and feel free to fork!
*   📐 **Missing Value Imputation · Outlier Treatment · Data Cleaning · Scikit-Learn**
