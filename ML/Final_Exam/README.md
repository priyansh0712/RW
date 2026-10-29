# Ames Housing Price Estimator — Supervised Learning Pipeline

End-to-end Machine Learning pipeline for residential property valuation benchmarked on the Ames Housing Dataset. Developed for PropTech platforms (comparable to NoBroker and MagicBricks) to provide real-time, automated property price estimations.

---

## 📌 Project Overview
- **Domain:** PropTech / Real Estate Automated Valuation Model (AVM)
- **Dataset:** [Ames Housing Dataset (Kaggle / UCI)](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
- **Features:** 79 residential property characteristics (living area, quality ratings, age, amenities, neighborhood)
- **Target:** `SalePrice` (USD, continuous regression task)
- **Best Model:** Tuned XGBoost Regressor ($R^2 = 0.929$, RMSE = \$19,810)

---

## 🗂️ Project Structure

```text
├── Data/
│   ├── train.csv                      # Training dataset (1,460 instances, 81 columns)
│   └── test.csv                       # Test dataset (1,459 instances, 80 columns)
├── final_exam.ipynb                   # Primary executed Jupyter Notebook with EDA, modeling, plots
├── HousePrice_SupervisedLearning.ipynb# Fully executed notebook for GitHub submission
├── house_price_model.pkl              # Serialized end-to-end scikit-learn Pipeline
├── summary_report.md                  # Executive summary report (~450 words)
├── requirements.txt                   # Environment dependencies
└── README.md                          # Project documentation and guide
```

---

## 📊 Pipeline Workflow

1. **Exploratory Data Analysis (EDA):**
   - Target normality analysis (raw right-skewed distribution vs `log1p` transformed normal distribution).
   - Univariate analysis on top numerical and high-impact categorical features (`Neighborhood`, `BldgType`, `HouseStyle`).
   - Bivariate correlation heatmaps, boxplots, scatter plots, and leverage outlier identification.
2. **Preprocessing & Feature Engineering:**
   - Imputation of structural missingness (`None` for absent amenities, `0` for absent numeric measurements, median for continuous).
   - Pruning columns with >80% missing records (`PoolQC`, `MiscFeature`, `Alley`, `Fence`).
   - Outlier elimination: removed 2 extreme abnormal sale records (`GrLivArea > 4000` & `SalePrice < $300k`).
   - Feature engineering: `TotalSF`, `HouseAge`, `RemodAge`, `HasGarage`, `HasPool`.
   - Ordinal mapping for quality rankings, one-hot encoding for nominal categories, `log1p` normalization for skewed features, and `StandardScaler` on continuous inputs.
3. **Model Development & Benchmarking:**
   - **Baseline:** Ordinary Least Squares (OLS) Linear Regression
   - **Regularized:** Ridge Regression (L2) & Lasso Regression (L1 feature pruning)
   - **Ensemble Tree Models:** Random Forest Regressor & XGBoost Regressor
   - **Hyperparameter Optimization:** `RandomizedSearchCV` on XGBoost
4. **Model Diagnostics & Explainability:**
   - Residual analysis (Fitted vs Residuals, Histogram, Q-Q Plot) verifying homoscedasticity.
   - SHAP (SHapley Additive exPlanations) beeswarm and single-instance waterfall plots.
5. **Deployment:**
   - Production-ready `scikit-learn` Pipeline serialized with `joblib`.

---

## 📈 Model Performance Summary

| Model | RMSE ($) | MAE ($) | R² Score | 5-Fold CV (Log RMSE) | Training Time (s) |
|---|---|---|---|---|---|
| **Linear Regression** | \$22,670.76 | \$15,744.11 | 0.9070 | 0.1342 | 0.038s |
| **Ridge Regression** | \$20,532.41 | \$14,640.89 | 0.9237 | 0.1171 | 0.045s |
| **Lasso Regression** | \$20,114.80 | \$14,142.06 | 0.9268 | 0.1148 | 0.092s |
| **Random Forest** | \$23,288.94 | \$16,081.25 | 0.9018 | 0.1385 | 0.612s |
| **Champion (XGBoost)** | **\$19,810.01** | **\$13,446.72** | **0.9290** | **0.1132** | 0.540s |

---

## 🚀 How to Run

### 1. Prerequisites & Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/priyansh0712/RW.git
cd RW_Exam/ML/Final_Exam
pip install -r requirements.txt
```

### 2. Run the Notebook
Open either `final_exam.ipynb` or `HousePrice_SupervisedLearning.ipynb` in VS Code or Jupyter Lab:
```bash
jupyter notebook final_exam.ipynb
```

### 3. Load Model and Run Inference
```python
import joblib
import pandas as pd
import numpy as np

# Load trained pipeline
pipeline = joblib.load('house_price_model.pkl')

# Load sample property
sample = pd.read_csv('Data/test.csv').iloc[:1].copy()
sample['TotalSF'] = sample['TotalBsmtSF'] + sample['1stFlrSF'] + sample['2ndFlrSF']
sample['HouseAge'] = (sample['YrSold'] - sample['YearBuilt']).apply(lambda x: max(0, x))
sample['RemodAge'] = (sample['YrSold'] - sample['YearRemodAdd']).apply(lambda x: max(0, x))
sample['HasGarage'] = (sample['GarageArea'] > 0).astype(int)
sample['HasPool'] = (sample['PoolArea'] > 0).astype(int)

# Predict estimated market price (USD)
predicted_price = np.expm1(pipeline.predict(sample))
print(f"Estimated Property Value: ${predicted_price[0]:,.2f}")
```

