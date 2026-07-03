<p align="center">
  <img src="assets/header.svg" alt="Final Examination Banner" width="100%">
</p>

<img src="assets/title_overview.svg" alt="Project Overview" width="100%">

This project is the **Final Examination** for Mathematics for Data Science, applying core concepts of **Statistics, Probability, Distributions, and Linear Algebra** to a real-world Loan Applications dataset (5,000 records, 7 features). The exam consists of **Part A (Theory)** and **Part B (Practical)** components.

The implementation is done in Python using a Jupyter Notebook (`exam.ipynb`).

---

<img src="assets/title_tools.svg" alt="Tools Used" width="100%">

<p align="left">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-3F3F3F?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Notebook">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/scipy-%238CA4F5.svg?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy">
  <img src="https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>

---

<img src="assets/title_part_a.svg" alt="Part A - Theory" width="100%">

### Q1. Explain Mean, Median, Mode in the context of customer income.

> **Ans:** Mean is the average income, Median is the middle value when sorted, and Mode is the most frequent income — from the dataset: Mean ≈ ₹69,418, Median ≈ ₹69,237, Mode = ₹15,000.

<img src="assets/q1_mean_median_mode.svg" alt="Mean Median Mode" width="100%">

---

### Q2. Differentiate between Standard Deviation and Variance using loan amounts.

> **Ans:** Variance measures average squared deviation from the mean (₹² units), while Standard Deviation is its square root in original units — Variance ≈ 770,245,609.88, Std Dev ≈ ₹27,753.30.

<img src="assets/q2_std_dev_variance.svg" alt="Standard Deviation & Variance" width="100%">

---

### Q3. What is a Random Variable? Give one example from the dataset.

> **Ans:** A Random Variable is a numerical quantity whose value depends on a random outcome — e.g., `Default_Status` (1 = Yes, 0 = No) is a discrete random variable, and `Income` is a continuous one.

<img src="assets/q3_random_variable.svg" alt="Random Variables" width="100%">

---

### Q4. Explain Conditional Probability in terms of loan defaults.

> **Ans:** Conditional Probability P(A|B) is the probability of event A given B has occurred — P(Default | Credit Score < 600) ≈ 39.53%, more than double the overall 18.52% default rate.

<img src="assets/q4_conditional_probability.svg" alt="Conditional Probability" width="100%">

---

### Q5. Define Bayes' Theorem and mention how banks can apply it.

> **Ans:** Bayes' Theorem: P(A|B) = [P(B|A) × P(A)] / P(B) — banks use it to calculate P(Default | Low Score) from known prior probabilities for credit risk assessment and fraud detection.

<img src="assets/q5_bayes_theorem.svg" alt="Bayes' Theorem" width="100%">

---

### Q6. Differentiate between Empirical Probability and Theoretical Probability with examples.

> **Ans:** Theoretical probability is based on mathematical reasoning (e.g., coin flip = 0.5), while Empirical probability is from observed data — e.g., loan default rate = 926/5000 ≈ 18.52%.

<img src="assets/q6_empirical_theoretical.svg" alt="Empirical vs Theoretical Probability" width="100%">

---

### Q7. What is a Poisson Distribution? Give a business example.

> **Ans:** Poisson Distribution models the count of rare events in a fixed interval (parameter λ) — e.g., a bank branch receiving an average of 5 loan applications/hour can predict staffing needs.

<img src="assets/q7_poisson_distribution.svg" alt="Poisson Distribution" width="100%">

---

### Q8. Write a short note on Eigenvalues and Eigenvectors in data analysis.

> **Ans:** For matrix A, eigenvector v satisfies Av = λv — they power PCA (dimensionality reduction), spectral clustering, and help identify principal components capturing maximum variance.

<img src="assets/q8_eigenvalues_eigenvectors.svg" alt="Eigenvalues & Eigenvectors" width="100%">

---

<img src="assets/title_part_b.svg" alt="Part B - Practical Tasks" width="100%">

### 📊 Task 1: Import Statements & Data Preview
<img src="image/Screenshot 2026-07-03 175327.png" alt="Import and Data Preview" width="100%">

---

### 📈 Task 2: Central Tendency & Dispersion
<img src="image/Screenshot 2026-07-03 175339.png" alt="Central Tendency and Dispersion" width="100%">

---

### 🎲 Task 3: Probability & Events
<img src="image/Screenshot 2026-07-03 175353.png" alt="Probability and Events" width="100%">

---

### 📉 Task 4: Distribution & Visualization
<img src="image/Screenshot 2026-07-03 175431.png" alt="Distribution and Visualization" width="100%">

---

### 🔢 Task 5: Linear Algebra Applications
<img src="image/Screenshot 2026-07-03 175449.png" alt="Linear Algebra Applications" width="100%">

---

<img src="assets/title_insights.svg" alt="Key Insights" width="100%">

*   ✔ **High Default Risk in Low Credit Scores**: Customers with Credit Score < 600 have a **39.53%** chance of default — more than double the overall rate of 18.52%.
*   ✔ **Symmetric Income Distribution**: Mean (₹69,418) and Median (₹69,237) are nearly identical, but Mode (₹15,000) reveals a cluster of low-income applicants.
*   ✔ **Right-Skewed Loan Amounts**: Skewness of **0.79** indicates some customers borrow significantly more than average; Kurtosis of **0.29** shows fewer extreme outliers.
*   ✔ **Customer Profile Similarity**: The **15.62°** angle between Customer 1 and 2's financial vectors shows very similar borrowing-to-income profiles.
*   ✔ **Normal Income Distribution**: The QQ Plot confirms income is approximately normally distributed, validating parametric statistical tests.

---

<img src="assets/title_results.svg" alt="Key Results" width="100%">

### 📊 Key Findings

*   ✔ **Central Tendency**: Mean Income ≈ ₹69,418 | Median ≈ ₹69,237 | Mode = ₹15,000
*   ✔ **Dispersion**: Loan Amount Range = ₹165,807 | Std Dev ≈ ₹27,753
*   ✔ **Default Probability**: Overall = 18.52% | Low Credit Score = 39.53%
*   ✔ **Distribution Shape**: Skewness = 0.79 (right-skewed) | Kurtosis = 0.29 (platykurtic)
*   ✔ **Vector Analysis**: Dot Product = 22,664,223,807 | L2 Norm = 140,359.48 | Angle = 15.62°

### 🎯 Final Conclusion

This examination successfully applied core Mathematics for Data Science concepts to the Loan Applications dataset. Statistical measures (mean, median, mode, variance, standard deviation) provided insights into customer income and loan distributions. Probability analysis revealed that low credit scores are a strong predictor of loan default. Distribution visualization confirmed approximate normality in income data. Linear algebra techniques (vector operations, norms, dot products) demonstrated how customer financial profiles can be mathematically compared for segmentation and risk assessment.

---

### 👤 Priyansh Vekariya

*   📍 Ahmedabad, Gujarat, India
*   ⭐ If you found this project helpful, give it a star and feel free to fork!
*   📐 **Statistics · Probability · Distributions · Linear Algebra**
