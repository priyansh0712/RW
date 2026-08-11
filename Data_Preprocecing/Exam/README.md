# 🚖 Urban Ride-Sharing Data Preprocessing Pipeline

<br>

## 📋 Project Overview

This project is the **Final Examination** for Data Preprocessing, building an **end-to-end Data Preprocessing & Feature Engineering pipeline** applied to an Urban Ride-Sharing dataset. It covers acquiring raw data from **three distinct source types** (CSV, JSON, and SQL/SQLite), performing deep data understanding & profiling, handling missing values with multiple imputation strategies, detecting and treating outliers, encoding categorical and numerical variables, applying feature scaling, and executing advanced transformations with engineered features.

The implementation is done in Python using a Jupyter Notebook — **[exam.ipynb](exam.ipynb)**.

<br>

---

## 🛠️ Tools & Technologies Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/Jupyter-3F3F3F?style=for-the-badge&logo=jupyter&logoColor=F37626">
  <img src="https://img.shields.io/badge/Pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-%23013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white">
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/ydata--profiling-3B82F6?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

<br>

---

## 📂 Dataset Overview

Three distinct data sources were integrated into pandas DataFrames:

| Source | Format | File / Endpoint | Dataset |
|--------|--------|-----------------|---------|
| 🟢 **CSV** | Flat file | [riders.csv](Data/riders%20-%20riders.csv.csv) | 300 riders · 9 columns |
| 🟡 **JSON** | Nested document | [trips.json](Data/trips.json) | 2,000 trips · 9 columns |
| 🔴 **SQL** | SQLite Database | [city_zones.sql](Data/city_zones.sql) | 10 zones · 5 columns |

### Riders Dataset (CSV — 300 records)

| Column | Type | Description |
|--------|------|-------------|
| `rider_id` | object | Unique rider identifier |
| `name` | object | Rider full name |
| `age` | int64 | Rider age |
| `gender` | object | Gender (Male / Female / Other) |
| `city` | object | City of residence |
| `signup_date` | object | Account signup date |
| `total_rides` | int64 | Total rides taken |
| `cancelled_rides` | int64 | Number of cancelled rides |
| `avg_rating` | float64 | Average rider rating |

### Trips Dataset (JSON — 2,000 records)

| Column | Type | Description |
|--------|------|-------------|
| `trip_id` | object | Unique trip identifier |
| `rider_id` | object | Reference to rider |
| `zone` | object | City zone of trip |
| `distance_km` | float64 | Trip distance (km) |
| `duration_min` | float64 | Trip duration (minutes) |
| `fare_amount` | float64 | Fare charged (₹) |
| `payment_mode` | object | Payment method (Cash / UPI) |
| `ride_date` | object | Date of ride |
| `surge_flag` | int64 | Surge pricing flag (0/1) |

### City Zones Dataset (SQL — 10 records)

| Column | Type | Description |
|--------|------|-------------|
| `zone_name` | object | Zone identifier (Zone_1 … Zone_10) |
| `population_density` | int64 | Population density per zone |
| `traffic_index` | float64 | Traffic congestion index |
| `avg_speed_kmph` | float64 | Average speed (km/h) |
| `zone_type` | object | Zone classification (Residential / Business) |

```python
# Data Acquisition
df = pd.read_csv("Data/riders - riders.csv.csv")

with open("Data/trips.json", "r") as file:
    metadata = json.load(file)
metadata_df = pd.DataFrame(metadata)

conn = sqlite3.connect("city_zones.db")
with open("Data/city_zones.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()
conn.executescript(sql_script)
zones_df = pd.read_sql("SELECT * FROM city_zones", conn)
```

<br>

---

## 🧹 Part 2 — Missing Value Imputation & Data Cleaning

Five imputation and cleaning strategies were applied:

| # | Strategy | Applied To | Method |
|---|----------|-----------|--------|
| 1 | 📊 **Mean Imputation** | Numeric columns | `SimpleImputer(strategy='mean')` |
| 2 | 📋 **Mode Imputation** | Categorical columns | `SimpleImputer(strategy='most_frequent')` |
| 3 | 🔗 **KNN Imputation** | `duration_min`, `distance_km`, `fare_amount` | `KNNImputer(n_neighbors=5)` |
| 4 | 📅 **Date Conversion** | `ride_date`, `signup_date` | `pd.to_datetime()` |
| 5 | 🚫 **Unrealistic Value Removal** | `fare_amount`, `distance_km` | Manual filtering |

```python
# Mean imputation for numeric columns
num_imputer = SimpleImputer(strategy='mean')
metadata_df[numeric_cols] = num_imputer.fit_transform(metadata_df[numeric_cols])

# Mode imputation for categorical columns
cat_imputer = SimpleImputer(strategy='most_frequent')
metadata_df[categorical_cols] = cat_imputer.fit_transform(metadata_df[categorical_cols])

# KNN Imputation for multivariate columns
knn_imputer = KNNImputer(n_neighbors=5)
metadata_df[knn_cols] = knn_imputer.fit_transform(metadata_df[knn_cols])
```

<br>

---

## 📊 Part 3 — Outlier Detection & Treatment

Three outlier handling techniques were applied:

| Technique | Column | Rule | Anomalies Found |
|-----------|--------|------|-----------------|
| 📐 **Z-Score** | `fare_amount` | \|z\| > 3 | 16 |
| 📐 **Z-Score** | `distance_km` | \|z\| > 3 | 3 |
| 📦 **IQR** | `duration_min` | Q1 − 1.5·IQR ≤ x ≤ Q3 + 1.5·IQR | 18 |
| 🔧 **Winsorization** | `fare_amount` | Cap at 1% tails | Applied |

**Before vs After Outlier Treatment:**

| Metric | fare_amount (Before) | fare_amount (After) |
|--------|---------------------|---------------------|
| **Mean** | 134.60 | 134.23 |
| **Std** | 85.52 | 84.22 |
| **Min** | 0.25 | 3.27 |
| **Max** | 472.29 | 379.63 |

```python
# Z-Score detection
fare_z = zscore(metadata_df['fare_amount'])
fare_anomalies = metadata_df[abs(fare_z) > 3]

# IQR for duration
Q1 = metadata_df['duration_min'].quantile(0.25)
Q3 = metadata_df['duration_min'].quantile(0.75)
IQR = Q3 - Q1
duration_anomalies = metadata_df[
    (metadata_df['duration_min'] < Q1 - 1.5 * IQR) |
    (metadata_df['duration_min'] > Q3 + 1.5 * IQR)
]

# Winsorization
metadata_df['fare_amount'] = winsorize(metadata_df['fare_amount'], limits=[0.01, 0.01])
```

<br>

---

## 🏷️ Part 4 — Feature Encoding & Engineering

### Categorical Encoding

| Technique | Column(s) | Method |
|-----------|-----------|--------|
| 🔢 **Label Encoding** | `gender` | `LabelEncoder()` |
| 📊 **Ordinal Encoding** | `traffic_level` | `OrdinalEncoder(categories=[['Low','Medium','High']])` |
| 🎯 **One-Hot Encoding** | `payment_mode`, `zone` | `pd.get_dummies(drop_first=False)` |

### Numerical Binning

| Technique | Column | Result |
|-----------|--------|--------|
| 🗂️ **Quantile Binning** | `total_rides` | Low / Medium / High |

### Date Feature Extraction

| Feature | Source | Method |
|---------|--------|--------|
| `hour` | `ride_date` | `.dt.hour` |
| `day_of_week` | `ride_date` | `.dt.dayofweek` |
| `month` | `ride_date` | `.dt.month` |

### Mathematical Transformations

| Transformation | Applied To | Purpose |
|----------------|-----------|---------|
| 📈 **Log (log1p)** | `fare_amount`, `distance_km` | Reduce right-skew |
| √ **Square Root** | `duration_min` | Moderate skew reduction |

```python
# Date extraction
metadata_df['hour'] = metadata_df['ride_date'].dt.hour
metadata_df['day_of_week'] = metadata_df['ride_date'].dt.dayofweek
metadata_df['month'] = metadata_df['ride_date'].dt.month

# Label Encoding
label_encoder = LabelEncoder()
df['gender'] = label_encoder.fit_transform(df['gender'])

# One-Hot Encoding
metadata_df = pd.get_dummies(metadata_df, columns=['payment_mode', 'zone'], drop_first=False)

# Log/Sqrt Transformations
metadata_df['fare_log'] = np.log1p(metadata_df['fare_amount'])
metadata_df['distance_log'] = np.log1p(metadata_df['distance_km'])
metadata_df['duration_sqrt'] = np.sqrt(metadata_df['duration_min'])
```

> 💡 **Result**: Final feature-engineered trips dataset expanded from 9 → 33 columns.

<br>

---

## ⚖️ Part 5 — Feature Scaling

Two scaling techniques were applied to all numeric columns:

| Technique | Description | Scikit-learn Class |
|-----------|-------------|---------------------|
| 📐 **Z-Score (Standardization)** | Mean = 0, Std = 1 | `StandardScaler()` |
| 📊 **Min-Max Scaling** | Scale to [0, 1] | `MinMaxScaler()` |

**Numeric columns scaled:** `distance_km`, `duration_min`, `fare_amount`, `population_density`, `traffic_index`, `avg_speed_kmph`

```python
scale_cols = ['distance_km', 'duration_min', 'fare_amount',
              'population_density', 'traffic_index', 'avg_speed_kmph']

# StandardScaler
standard_scaler = StandardScaler()
standard_df = pd.DataFrame(standard_scaler.fit_transform(metadata_df[scale_cols]),
                           columns=scale_cols, index=metadata_df.index)

# MinMaxScaler
minmax_scaler = MinMaxScaler()
minmax_df = pd.DataFrame(minmax_scaler.fit_transform(metadata_df[scale_cols]),
                         columns=scale_cols, index=metadata_df.index)
```

<br>

---

## 🔧 Part 6 — Feature Construction

Six business-meaningful features were engineered:

| Feature | Formula | Business Meaning |
|---------|---------|-----------------|
| `avg_ride_distance` | `total_distance / total_rides` | Average km per ride |
| `avg_ride_fare` | `total_fare / total_rides` | Average spend per ride |
| `is_peak_hour` | `hour ∈ {7,8,9,18,19,20,21}` | Peak hour flag |
| `days_since_signup` | `today − signup_date` | Customer tenure (days) |
| `ride_cancellation_rate` | `cancelled_rides / total_rides` | Cancellation ratio |
| `surge_flag` | `fare/distance > 95th percentile` | Price surge detection |

```python
# avg_ride_distance & avg_ride_fare
ride_distance = metadata_df.groupby('rider_id')['distance_km'].sum()
df['avg_ride_distance'] = df['rider_id'].map(ride_distance) / df['total_rides']

ride_fare = metadata_df.groupby('rider_id')['fare_amount'].sum()
df['avg_ride_fare'] = df['rider_id'].map(ride_fare) / df['total_rides']

# is_peak_hour
metadata_df['is_peak_hour'] = metadata_df['hour'].isin([7,8,9,18,19,20,21]).astype(int)

# days_since_signup
df['days_since_signup'] = (pd.Timestamp.today() - df['signup_date']).dt.days

# ride_cancellation_rate
df['ride_cancellation_rate'] = df['cancelled_rides'] / df['total_rides']
```

<br>

---

## 📦 Part 7 — Final Dataset & Auto-Profiling

The cleaned and enriched datasets were merged into a production-ready file:

| Metric | Before | After |
|--------|--------|-------|
| 📊 **Rows** | 2,000 | 2,000 |
| ❌ **Missing Values** | 0 | 0 |
| ⚙️ **Engineered Features** | 0 | 13 |
| 📐 **Total Columns** | 34 | 47 |

```python
# Merge cleaned & enriched datasets
final_df = metadata_df.merge(df, on='rider_id', how='left')

# Export final dataset
final_df.to_csv('final_prepared_rides_dataset.csv', index=False)

# Auto-Profiling with ydata-profiling
profile = ProfileReport(final_df, title="Ride Dataset EDA Report", explorative=True)
profile.to_file("ride_eda_report.html")
```

**Final Output Files:**
- [final_prepared_rides_dataset.csv](final_prepared_rides_dataset.csv) — Production-ready cleaned dataset
- [ride_eda_report.html](ride_eda_report.html) — Auto-generated EDA profiling report

<br>

---

## 📊 Key Findings

*   ✔ **Multi-Source Integration**: Three data sources (CSV, JSON, SQL) were seamlessly integrated into unified DataFrames for comprehensive analysis.
*   ✔ **Robust Imputation**: Mean, Mode, and KNN imputation strategies ensured zero data loss while preserving inter-variable relationships.
*   ✔ **Outlier Treatment**: Z-Score, IQR, and Winsorization detected 37 anomalies across fare, distance, and duration columns.
*   ✔ **Comprehensive Encoding**: Label, Ordinal, and One-Hot encoding handled all categorical variable types.
*   ✔ **Dual Scaling**: StandardScaler and MinMaxScaler applied across 6 numeric features for model readiness.
*   ✔ **Power Transformations**: Log and Square Root transforms reduced skewness in fare, distance, and duration distributions.
*   ✔ **Feature Engineering**: Six business-meaningful features created — `avg_ride_distance`, `avg_ride_fare`, `is_peak_hour`, `days_since_signup`, `ride_cancellation_rate`, and `surge_flag`.
*   ✔ **Auto-Profiling**: Full dataset profiled with ydata-profiling for automated EDA reporting.
*   ✔ **Final Dataset**: Cleaned, transformed, and exported as [final_prepared_rides_dataset.csv](final_prepared_rides_dataset.csv).

## 🎯 Final Conclusion

This project successfully demonstrated an end-to-end data preprocessing and feature engineering workflow on a multi-source Urban Ride-Sharing dataset. By acquiring data from CSV, JSON, and SQL sources, the pipeline covers the most common enterprise data formats. Multiple imputation strategies (Mean, Mode, KNN) preserved data integrity while resolving missing values. Outlier detection via Z-Score, IQR, and Winsorization ensured robust distributions. A comprehensive suite of encoding (Label, Ordinal, One-Hot) and scaling (StandardScaler, MinMaxScaler) techniques was applied, followed by power transformations (Log, Sqrt) to normalize skewed features. The workflow culminates in engineered features and a production-ready cleaned dataset suitable for any downstream ride-sharing analytics or modeling task.

<br>

---

### 👤 Priyansh Vekariya

*   📍 Ahmedabad, Gujarat, India
*   ⭐ If you found this project useful, give it a star and feel free to fork!
*   📐 **Data Acquisition · Imputation · Outlier Handling · Encoding · Scaling · Feature Engineering**
