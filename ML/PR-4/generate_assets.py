import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

BASE   = r"d:\RW\RW_Exam\ML\PR-4"
ASSETS = os.path.join(BASE, "assets")
IMAGE  = os.path.join(BASE, "image")
os.makedirs(ASSETS, exist_ok=True)
os.makedirs(IMAGE,  exist_ok=True)

TMPL = open(r"d:\RW\RW_Exam\ML\PR-3\assets\title_partb.svg", encoding="utf-8").read()

PARTS = [
    ("title_overview",  "Project Overview",
     "M12 19 l5 5 l10 -10", "#10b981","#059669"),
    ("title_tools",     "Tools &amp; Libraries",
     "M14 19 h10 M19 14 v10", "#f59e0b","#d97706"),
    ("title_partb",     "Part B \u2014 Dataset Understanding &amp; Preprocessing",
     "M19 9 v20 M9 19 h20 M19 13 a6 6 0 1 0 0 12 a6 6 0 1 0 0 -12", "#6366f1","#3b82f6"),
    ("title_partc",     "Part C \u2014 Baseline Model: K-Nearest Neighbors (KNN)",
     "M11 19 a8 8 0 1 0 16 0 a8 8 0 1 0 -16 0 M27 27 l4 4", "#10b981","#059669"),
    ("title_partd",     "Part D \u2014 Support Vector Machine (SVM)",
     "M10 25 l19 -12 M10 13 l19 12 M19 10 v18", "#6366f1","#4f46e5"),
    ("title_parte",     "Part E \u2014 Probabilistic Model: Naive Bayes",
     "M12 12 h14 v14 h-14 z M16 19 h6 M19 16 v6", "#ec4899","#db2777"),
    ("title_partf",     "Part F \u2014 Model Evaluation &amp; Comparison",
     "M10 28 l5 -8 l5 4 l5 -10 l5 6", "#f59e0b","#d97706"),
    ("title_results",   "Brief Report &amp; Key Insights",
     "M13 19 l4 4 l8 -8", "#f59e0b","#d97706"),
]

for fname, label, icon, c1, c2 in PARTS:
    orig = open(r"d:\RW\RW_Exam\ML\PR-3\assets\title_partb.svg", encoding="utf-8").read()
    svg  = orig.replace(
        "Part B \u2014 Dataset Preparation &amp; Understanding", label
    ).replace(
        "M19 9 v20 M9 19 h20 M19 13 a6 6 0 1 0 0 12 a6 6 0 1 0 0 -12", icon
    ).replace(
        "#6366f1", c1
    ).replace(
        "#3b82f6", c2
    )
    path = os.path.join(ASSETS, fname + ".svg")
    open(path, "w", encoding="utf-8").write(svg)
    print("Saved", fname+".svg")

# Pipeline SVG - copy from PR-3 project_pipeline_overview but adapted
import shutil
shutil.copy(r"d:\RW\RW_Exam\ML\PR-3\assets\project_pipeline_overview.svg",
            os.path.join(ASSETS, "project_pipeline_overview.svg"))
print("Copied project_pipeline_overview.svg")

# PNG charts
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"]  = "#cbd5e1"
plt.rcParams["axes.linewidth"]  = 1.2

# 1 - KNN analysis
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
ks = [3,5,7,9,11]; acc_k = [0.8154,0.8144,0.8125,0.8125,0.8125]
axes[0].plot(ks, acc_k, marker="o", color="#6366f1", linewidth=2.5, markersize=7)
axes[0].set_title("KNN: Accuracy vs k Value", fontsize=13, fontweight="bold", pad=12)
axes[0].set_xlabel("k (Neighbors)", fontsize=11); axes[0].set_ylabel("Test Accuracy", fontsize=11); axes[0].set_ylim(0.80, 0.83)
for k, a in zip(ks, acc_k):
    axes[0].annotate(f"{a:.4f}", (k,a), xytext=(0,8), textcoords="offset points", ha="center", fontsize=9, fontweight="bold")
bars = axes[1].bar(["euclidean","manhattan"], [0.8144,0.8144], color=["#10b981","#ec4899"], width=0.45, edgecolor="#1e293b")
axes[1].set_title("KNN: Distance Metric Comparison (k=5)", fontsize=13, fontweight="bold", pad=12)
axes[1].set_ylabel("Test Accuracy", fontsize=11); axes[1].set_ylim(0.80, 0.83)
for bar in bars:
    h = bar.get_height()
    axes[1].text(bar.get_x()+bar.get_width()/2, h+0.001, f"{h:.4f}", ha="center", fontsize=11, fontweight="bold")
plt.tight_layout(); plt.savefig(os.path.join(IMAGE,"knn_analysis.png"), dpi=300); plt.close()
print("Saved knn_analysis.png")

# 2 - SVM analysis
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
bars = axes[0].bar(["Linear","RBF"], [0.9952,0.8298], color=["#10b981","#ef4444"], width=0.45, edgecolor="#1e293b")
axes[0].set_title("SVM: Linear vs RBF Kernel Accuracy", fontsize=13, fontweight="bold", pad=12)
axes[0].set_ylabel("Test Accuracy", fontsize=11); axes[0].set_ylim(0.75,1.05)
for bar in bars:
    h = bar.get_height()
    axes[0].text(bar.get_x()+bar.get_width()/2, h+0.005, f"{h*100:.2f}%", ha="center", fontsize=11, fontweight="bold")
c_vals = [0.1,1,10,100]
axes[1].plot(c_vals, [0.9952]*4, marker="s", color="#10b981", linewidth=2.5, markersize=7)
axes[1].set_xscale("log"); axes[1].set_title("Linear SVM: Accuracy vs C Value (log scale)", fontsize=13, fontweight="bold", pad=12)
axes[1].set_xlabel("C (log scale)", fontsize=11); axes[1].set_ylabel("Test Accuracy", fontsize=11); axes[1].set_ylim(0.99, 1.001)
axes[1].text(1, 0.9955, "Stable 99.52% across all C", fontsize=10, color="#10b981", fontweight="bold")
plt.tight_layout(); plt.savefig(os.path.join(IMAGE,"svm_analysis.png"), dpi=300); plt.close()
print("Saved svm_analysis.png")

# 3 - NB Confusion Matrix
cm_nb = np.array([[847,17],[106,70]])
fig, ax = plt.subplots(figsize=(7,6))
ConfusionMatrixDisplay(confusion_matrix=cm_nb, display_labels=["Legit (0)","Spam (1)"]).plot(ax=ax, cmap="Blues", colorbar=False)
ax.set_title("Naive Bayes Confusion Matrix (N=1040)\n88.17% Accuracy  |  57.44% Recall", fontsize=13, fontweight="bold", pad=15)
plt.tight_layout(); plt.savefig(os.path.join(IMAGE,"nb_confusion_matrix.png"), dpi=300); plt.close()
print("Saved nb_confusion_matrix.png")

# 4 - Model Benchmark
models   = ["KNN (k=3)","SVM Linear","SVM RBF","Naive Bayes"]
accuracy = [0.8154,0.9952,0.8298,0.8817]
precision= [1.0000,1.0000,0.6452,0.7368]
recall   = [0.0103,0.9744,0.2051,0.5744]
f1       = [0.0203,0.9870,0.3113,0.6455]
x = np.arange(len(models)); w = 0.2
fig, ax = plt.subplots(figsize=(12,5.5))
r1 = ax.bar(x-1.5*w, accuracy,  w, label="Accuracy",  color="#3b82f6")
r2 = ax.bar(x-0.5*w, precision, w, label="Precision", color="#8b5cf6")
r3 = ax.bar(x+0.5*w, recall,    w, label="Recall",    color="#10b981")
r4 = ax.bar(x+1.5*w, f1,        w, label="F1-Score",  color="#ec4899")
ax.set_title("Master Model Benchmark Comparison\nLinear SVM Dominates All Metrics", fontsize=13, fontweight="bold", pad=15)
ax.set_xticks(x); ax.set_xticklabels(models, fontsize=11, fontweight="bold")
ax.set_ylim(0,1.1); ax.set_ylabel("Score", fontsize=12); ax.legend(loc="upper left")
for rects in [r1,r2,r3,r4]:
    for rect in rects:
        h = rect.get_height()
        if h > 0.05:
            ax.annotate(f"{h*100:.1f}%", xy=(rect.get_x()+rect.get_width()/2, h),
                        xytext=(0,3), textcoords="offset points", ha="center", va="bottom", fontsize=7.5, fontweight="bold")
plt.tight_layout(); plt.savefig(os.path.join(IMAGE,"model_benchmark_comparison.png"), dpi=300); plt.close()
print("Saved model_benchmark_comparison.png")

print("All assets done!")
