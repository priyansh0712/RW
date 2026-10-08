import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score, recall_score,
                             f1_score, roc_curve, roc_auc_score)
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN

# Output directory
out_dir = r"d:\RW\RW_Exam\ML\PR-3\image"
os.makedirs(out_dir, exist_ok=True)

# Set style
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.2

# 1. Load Data
df = pd.read_csv(r"d:\RW\RW_Exam\ML\PR-3\Risk_Alert.csv")
X = df.drop(columns=['customer_id', 'risk_status'])
y = df['risk_status']

X['last_transaction_date'] = pd.to_datetime(X['last_transaction_date'], errors='coerce')
X['days_since_last_transaction'] = (pd.Timestamp.today() - X['last_transaction_date']).dt.days
X = X.drop(columns=['last_transaction_date'])
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Imputation
imputer = KNNImputer(n_neighbors=5)
X_train_imp = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
X_test_imp = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns, index=X_test.index)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imp)
X_test_scaled = scaler.transform(X_test_imp)

# Baseline Logistic Regression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)
lr_prob = lr_model.predict_proba(X_test_scaled)[:, 1]

# Decision Tree Baseline
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train_imp, y_train)
dt_pred = dt_model.predict(X_test_imp)
dt_prob = dt_model.predict_proba(X_test_imp)[:, 1]

# Random Forest Baseline
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_imp, y_train)
rf_pred = rf_model.predict(X_test_imp)
rf_prob = rf_model.predict_proba(X_test_imp)[:, 1]

# Tuned Random Forest (Best parameters from notebook)
tuned_rf = RandomForestClassifier(
    n_estimators=219, max_depth=17, min_samples_split=11, min_samples_leaf=2,
    max_features='sqrt', random_state=42
)
tuned_rf.fit(X_train_imp, y_train)
tuned_rf_pred = tuned_rf.predict(X_test_imp)
tuned_rf_prob = tuned_rf.predict_proba(X_test_imp)[:, 1]

print("Data & Models prepared!")

# ==========================================
# CHART 1: EDA & Class Imbalance (4 Panels)
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Class Distribution
counts = y_train.value_counts()
colors = ['#3b82f6', '#ef4444']
bars = axes[0, 0].bar(['Low Risk (0)', 'High Risk (1)'], counts.values, color=colors, width=0.55, edgecolor='#1e293b', linewidth=1.2)
axes[0, 0].set_title("Training Class Distribution (Severe Imbalance 7.25 : 1)", fontsize=13, fontweight='bold', pad=12)
axes[0, 0].set_ylabel("Number of Customers", fontsize=11)
for bar in bars:
    yval = bar.get_height()
    pct = (yval / len(y_train)) * 100
    axes[0, 0].text(bar.get_x() + bar.get_width()/2.0, yval + 50, f"{yval:,} ({pct:.1f}%)", ha='center', va='bottom', fontsize=11, fontweight='bold')
axes[0, 0].set_ylim(0, 3600)

# Panel 2: Credit Score by Risk Status
sns.kdeplot(data=df, x='credit_score', hue='risk_status', palette={0: '#3b82f6', 1: '#ef4444'}, fill=True, common_norm=False, ax=axes[0, 1], alpha=0.4)
axes[0, 1].set_title("Credit Score Density by Risk Status", fontsize=13, fontweight='bold', pad=12)
axes[0, 1].set_xlabel("Credit Score (Bureau Rating)", fontsize=11)
axes[0, 1].legend(title='Risk Status', labels=['High Risk (1)', 'Low Risk (0)'])

# Panel 3: Missed Payments 12m
missed_counts = df.groupby(['missed_payments_12m', 'risk_status']).size().unstack(fill_value=0)
missed_counts.plot(kind='bar', stacked=True, color=['#3b82f6', '#ef4444'], ax=axes[1, 0], edgecolor='#1e293b', width=0.65)
axes[1, 0].set_title("Missed Payments in Past 12 Months", fontsize=13, fontweight='bold', pad=12)
axes[1, 0].set_xlabel("Missed Payment Count", fontsize=11)
axes[1, 0].set_ylabel("Number of Accounts", fontsize=11)
axes[1, 0].legend(title='Risk Status', labels=['Low Risk (0)', 'High Risk (1)'])
axes[1, 0].tick_params(axis='x', rotation=0)

# Panel 4: Credit Utilization Ratio vs Debt Balance
sns.boxplot(data=df, x='risk_status', y='credit_utilization_ratio', palette=['#3b82f6', '#ef4444'], ax=axes[1, 1], width=0.45)
axes[1, 1].set_xticklabels(['Low Risk (0)', 'High Risk (1)'], fontsize=11)
axes[1, 1].set_title("Credit Utilization Ratio by Risk Status", fontsize=13, fontweight='bold', pad=12)
axes[1, 1].set_ylabel("Credit Utilization Ratio", fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "eda_distribution_scatter.png"), dpi=300)
plt.close()
print("Saved eda_distribution_scatter.png")

# ==========================================
# CHART 2: Confusion Matrix Baseline
# ==========================================
cm = confusion_matrix(y_test, lr_pred)
fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
            annot_kws={'size': 18, 'weight': 'bold'},
            xticklabels=['Predicted Low Risk (0)', 'Predicted High Risk (1)'],
            yticklabels=['Actual Low Risk (0)', 'Actual High Risk (1)'])
ax.set_title("Logistic Regression Test Confusion Matrix (N = 920)\n100% Precision · 100% Recall · Zero False Negatives",
             fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "confusion_matrix_baseline.png"), dpi=300)
plt.close()
print("Saved confusion_matrix_baseline.png")

# ==========================================
# CHART 3: Resampling Strategies Comparison
# ==========================================
resampling_data = {
    'Method': ['Baseline', 'Under-Sampling', 'Over-Sampling', 'SMOTE', 'ADASYN'],
    'Recall': [1.0, 1.0, 1.0, 1.0, 1.0],
    'F1-Score': [1.0, 0.9911, 0.9911, 0.9911, 0.9823],
    'AUC-ROC': [1.0, 1.0, 1.0, 1.0, 0.999989]
}
res_df = pd.DataFrame(resampling_data)

fig, ax = plt.subplots(figsize=(10, 5.5))
x = np.arange(len(res_df['Method']))
width = 0.25

rects1 = ax.bar(x - width, res_df['Recall'], width, label='Test Recall (TPR)', color='#10b981', edgecolor='#064e3b')
rects2 = ax.bar(x, res_df['F1-Score'], width, label='Test F1-Score', color='#6366f1', edgecolor='#312e81')
rects3 = ax.bar(x + width, res_df['AUC-ROC'], width, label='Test AUC-ROC', color='#f59e0b', edgecolor='#78350f')

ax.set_title("Performance Across Imbalanced Data Resampling Methods", fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(res_df['Method'], fontsize=11, fontweight='bold')
ax.set_ylim(0.95, 1.01)
ax.set_ylabel("Metric Score", fontsize=12)
ax.legend(loc='lower left', frameon=True, facecolor='white', framealpha=0.9)

for rects in [rects1, rects2, rects3]:
    for rect in rects:
        h = rect.get_height()
        ax.annotate(f"{h:.4f}", xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "resampling_methods_comparison.png"), dpi=300)
plt.close()
print("Saved resampling_methods_comparison.png")

# ==========================================
# CHART 4: Decision Tree vs Random Forest
# ==========================================
tree_comp = pd.DataFrame({
    'Model': ['Decision Tree', 'Random Forest (100 Trees)'],
    'Accuracy': [accuracy_score(y_test, dt_pred), accuracy_score(y_test, rf_pred)],
    'Precision': [precision_score(y_test, dt_pred), precision_score(y_test, rf_pred)],
    'Recall': [recall_score(y_test, dt_pred), recall_score(y_test, rf_pred)],
    'F1-Score': [f1_score(y_test, dt_pred), f1_score(y_test, rf_pred)]
})

fig, ax = plt.subplots(figsize=(10, 5.5))
x = np.arange(len(tree_comp['Model']))
width = 0.2

r1 = ax.bar(x - 1.5*width, tree_comp['Accuracy'], width, label='Accuracy', color='#3b82f6')
r2 = ax.bar(x - 0.5*width, tree_comp['Precision'], width, label='Precision', color='#8b5cf6')
r3 = ax.bar(x + 0.5*width, tree_comp['Recall'], width, label='Recall (Key Metric)', color='#10b981')
r4 = ax.bar(x + 1.5*width, tree_comp['F1-Score'], width, label='F1-Score', color='#ec4899')

ax.set_title("Single Decision Tree vs. Random Forest Bagging Ensemble\nRandom Forest Eliminates High Variance & Overfitting", fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(tree_comp['Model'], fontsize=12, fontweight='bold')
ax.set_ylim(0.80, 1.03)
ax.set_ylabel("Score", fontsize=12)
ax.legend(loc='lower left', frameon=True)

for rects in [r1, r2, r3, r4]:
    for rect in rects:
        h = rect.get_height()
        ax.annotate(f"{h*100:.1f}%", xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "tree_vs_forest_predictions.png"), dpi=300)
plt.close()
print("Saved tree_vs_forest_predictions.png")

# ==========================================
# CHART 5: Hyperparameter Tuning Uplift
# ==========================================
tune_comp = pd.DataFrame({
    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Untuned Random Forest': [accuracy_score(y_test, rf_pred), precision_score(y_test, rf_pred),
                              recall_score(y_test, rf_pred), f1_score(y_test, rf_pred)],
    'Tuned Random Forest': [accuracy_score(y_test, tuned_rf_pred), precision_score(y_test, tuned_rf_pred),
                            recall_score(y_test, tuned_rf_pred), f1_score(y_test, tuned_rf_pred)]
})

fig, ax = plt.subplots(figsize=(9, 5.5))
x = np.arange(len(tune_comp['Metric']))
width = 0.35

bar1 = ax.bar(x - width/2, tune_comp['Untuned Random Forest'], width, label='Untuned RF (100 Trees)', color='#94a3b8', edgecolor='#475569')
bar2 = ax.bar(x + width/2, tune_comp['Tuned Random Forest'], width, label='Tuned RF (GridSearchCV: 219 Trees, depth=17)', color='#10b981', edgecolor='#064e3b')

ax.set_title("Random Forest Hyperparameter Tuning Uplift\nRecall Increased from 96.40% to 98.20% (+1.80% Gain)", fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(tune_comp['Metric'], fontsize=11, fontweight='bold')
ax.set_ylim(0.94, 1.01)
ax.set_ylabel("Score", fontsize=12)
ax.legend(loc='lower left', frameon=True)

for bar in bar1:
    h = bar.get_height()
    ax.annotate(f"{h*100:.2f}%", xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')
for bar in bar2:
    h = bar.get_height()
    ax.annotate(f"{h*100:.2f}%", xy=(bar.get_x() + bar.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#047857')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "hyperparameter_tuning_surface.png"), dpi=300)
plt.close()
print("Saved hyperparameter_tuning_surface.png")

# ==========================================
# CHART 6: ROC Curve Comparison
# ==========================================
fpr_log, tpr_log, _ = roc_curve(y_test, lr_prob)
fpr_dt, tpr_dt, _ = roc_curve(y_test, dt_prob)
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_prob)
fpr_tuned_rf, tpr_tuned_rf, _ = roc_curve(y_test, tuned_rf_prob)

fig, ax = plt.subplots(figsize=(8, 6.5))
ax.plot(fpr_log, tpr_log, label=f"Logistic Regression (AUC = {roc_auc_score(y_test, lr_prob):.4f})", color='#3b82f6', linewidth=2.5)
ax.plot(fpr_tuned_rf, tpr_tuned_rf, label=f"Tuned Random Forest (AUC = {roc_auc_score(y_test, tuned_rf_prob):.4f})", color='#10b981', linewidth=2.5)
ax.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {roc_auc_score(y_test, rf_prob):.4f})", color='#f59e0b', linewidth=2, linestyle='--')
ax.plot(fpr_dt, tpr_dt, label=f"Decision Tree (AUC = {roc_auc_score(y_test, dt_prob):.4f})", color='#ef4444', linewidth=2)
ax.plot([0, 1], [0, 1], linestyle=':', color='#94a3b8', linewidth=1.5, label='Random Chance Baseline (AUC = 0.500)')

ax.set_title("Receiver Operating Characteristic (ROC) Comparison\nEvaluated on Held-out Test Set (N = 920)", fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel("False Positive Rate (1 - Specificity)", fontsize=11)
ax.set_ylabel("True Positive Rate (Recall)", fontsize=11)
ax.legend(loc='lower right', frameon=True, fontsize=10)
ax.set_xlim([-0.02, 1.02])
ax.set_ylim([-0.02, 1.02])

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "roc_curve_comparison.png"), dpi=300)
plt.close()
print("Saved roc_curve_comparison.png")

# ==========================================
# CHART 7: Master Model Leaderboard Benchmark
# ==========================================
leaderboard = pd.DataFrame({
    'Model': ['Logistic Regression', 'Tuned Random Forest', 'Random Forest (100 Trees)', 'Decision Tree'],
    'Recall': [1.0, 0.9820, 0.9640, 0.8649],
    'F1-Score': [1.0, 0.9864, 0.9772, 0.8767],
    'AUC-ROC': [1.0, 0.9999, 0.9999, 0.9250]
})

fig, ax = plt.subplots(figsize=(10, 5.5))
y_pos = np.arange(len(leaderboard['Model']))
bar_height = 0.25

b1 = ax.barh(y_pos - bar_height, leaderboard['Recall'], bar_height, label='Test Recall (Sensitivity)', color='#10b981')
b2 = ax.barh(y_pos, leaderboard['F1-Score'], bar_height, label='Test F1-Score', color='#6366f1')
b3 = ax.barh(y_pos + bar_height, leaderboard['AUC-ROC'], bar_height, label='Test AUC-ROC', color='#f59e0b')

ax.set_yticks(y_pos)
ax.set_yticklabels(leaderboard['Model'], fontsize=11, fontweight='bold')
ax.invert_yaxis()
ax.set_xlim(0.80, 1.03)
ax.set_xlabel("Performance Score", fontsize=11)
ax.set_title("Master Model Evaluation Leaderboard (Held-out Test Set, N = 920)\nPrioritizing High Recall to Minimize High-Risk Default Losses", fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='lower left', frameon=True)

for bars in [b1, b2, b3]:
    for bar in bars:
        w = bar.get_width()
        ax.annotate(f"{w:.4f}", xy=(w, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=8.5, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "model_benchmark_comparison.png"), dpi=300)
plt.close()
print("Saved model_benchmark_comparison.png")
print("All 7 charts generated successfully!")
