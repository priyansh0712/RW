<p align="center">
  <img src="assets/header.svg" alt="Calculative Foundation Banner" width="100%">
</p>

<img src="assets/title_overview.svg" alt="Project Overview" width="100%">

This project applies fundamental and advanced **Linear Algebra** concepts to represent, analyze, and transform a student performance dataset. By mapping students' subject scores to vectors and matrices, we perform operations like projections, norms, decompositions (LU, SVD), and dimensionality reduction (PCA, LDA) to extract meaningful academic insights.

The implementation is done in Python using a Jupyter Notebook.


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
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
</p>

---

<img src="assets/title_demo.svg" alt="Visual Demonstration" width="100%">

<video src="assets/20260702-1443-44.7086436.mp4" width="100%" controls autoplay loop muted></video>

---

<img src="assets/title_structure.svg" alt="Project Structure &amp; Tasks" width="100%">

### 📐 Part A: Vector & Matrix Fundamentals
Each student's subject scores are represented as a vector: $\vec{v} = [x_{\text{Math}}, y_{\text{Science}}, z_{\text{English}}]$.

*   **Vector Norms**:
    *   **L1 Norm (Manhattan Distance)**: Measures total academic load.
        $$\|\vec{v}\|_1 = \sum_{i=1}^n |v_i|$$
    *   **L2 Norm (Euclidean Distance)**: Represents overall academic strength as a vector distance from origin.
        $$\|\vec{v}\|_2 = \sqrt{\sum_{i=1}^n v_i^2}$$
*   **Dot Product & Angle**: Evaluates similarity in performance profiles.
    $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta \implies \theta = \arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$$
*   **Vector Projection**: Measures relative alignment of one student's scores onto another.
    $$\text{proj}_{\vec{u}}\vec{v} = \left(\frac{\vec{v} \cdot \vec{u}}{\|\vec{u}\|^2}\right) \vec{u}$$
*   **Cross Product**: Computes a normal vector in 3D space indicating orthogonal academic paths.
*   **Visualizations**:
    *   **2D Vector Plot**: Representing Math vs Science.
    *   **3D Vector Plot**: 3D spatial plotting of Math, Science, and English.

### 🧮 Part B: Matrix Operations
We construct a Student-Subject matrix $A$ of dimensions $M \times N$ (rows: students, columns: subjects).
*   **Matrix Multiplication**: Computes the student-to-student similarity matrix via $A \cdot A^T$.
*   **Transpose**: Swapping axes $A^T$ to pivot between student-centric and subject-centric views.
*   **Determinant & Inverse**: Solving systems of equations $A\vec{x} = \vec{b}$ and ensuring linear independence:
    $$\det(A) \neq 0 \implies A^{-1} \text{ exists}$$
*   **Heatmap Visualization**: Plotting score matrices using `plt.imshow()` with annotated score values.

### 🌐 Part C: Linear Transformations & Geometry
Interpreting geometric subspaces spanned by student databases:
*   **Line (1D/2D Subspace)**: Progression profile over 2 subjects.
*   **Plane (3D Subspace)**: Progression profile over 3 subjects.
*   **Hyperplane ($N$-D Space)**: Complex multi-dimensional representations (4+ subjects).

### 🔑 Part D: Eigenvalues & Decomposition
*   **Covariance Matrix**: Analyzing statistical score co-movements:
    $$\Sigma = \frac{1}{M-1} X^T X$$
*   **Eigenvalues & Eigenvectors**: Extracting axes of principal variation (academic profile traits):
    $$A\vec{v} = \lambda\vec{v}$$
*   **LU Decomposition**: Decomposing matrix $A$ into Lower ($L$) and Upper ($U$) triangular components with permutation $P$:
    $$P A = L U$$
*   **Singular Value Decomposition (SVD)**: Decomposing to reveal hidden student groupings:
    $$A = U \Sigma V^T$$

### 📉 Part E: Dimensionality Reduction
*   **Principal Component Analysis (PCA)**: Projecting students into a 2D space of maximum variance (PC1 vs PC2) to simplify evaluation.
*   **Linear Discriminant Analysis (LDA)**: Finding a projection vector that maximizes separation between "Pass" and "Fail" academic tiers:
    $$J(\vec{w}) = \frac{\vec{w}^T S_B \vec{w}}{\vec{w}^T S_W \vec{w}}$$

---

<img src="assets/title_run.svg" alt="How to Run the Notebook" width="100%">

1.  **Clone the repository**:
    ```bash
    git clone <your-repo-link>
    cd PR_4
    ```
2.  **Install dependencies**:
    ```bash
    pip install numpy scipy matplotlib scikit-learn jupyter
    ```
3.  **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
4.  Open and run all cells in [pr_4.ipynb](file:///d:/RW/RW_Exam/Maths/PR_4/pr_4.ipynb).

---

<img src="assets/title_results.svg" alt="Key Results &amp; Interpretations" width="100%">

### 📊 Key Findings

*   ✔ **Vector Norms**: L2 Norm successfully quantified overall academic strength, showing Student A leads in score magnitude.
*   ✔ **Profile Similarity**: Vector angle showed Student A and Student B have highly correlated relative subject strengths ($11.59^\circ$ separation).
*   ✔ **Matrix Invertibility**: Matrix determinant confirmed that the student-subject vector spaces are linearly independent and invertible.
*   ✔ **Efficient Computation**: LU decomposition split the matrix into triangular components for fast computational solvability.
*   ✔ **Decomposition Analysis**: SVD successfully factored the grade matrix to highlight singular values ($\vec{\sigma} = [246.197, 19.957, 8.467]$).
*   ✔ **Principal Component**: PCA successfully captured over 99.4% of academic variance in the first principal component, representing general capability.
*   ✔ **Supervised Separation**: LDA successfully partitioned passing and failing students into clearly separated coordinate clusters.
*   ✔ **Data Extraction**: Linear algebra methods successfully transformed healthcare/student data into evidence-based insights.

### 🎯 Final Conclusion

This project successfully applied fundamental and advanced Linear Algebra techniques to a student performance database. Mathematical analyses including vector norms, projections, similarity matrix multiplication, covariance mapping, eigensystem extraction, LU/SVD matrix decompositions, PCA, and LDA were used to evaluate student-related academic dimensions.

The results showed that while students share highly similar relative academic distributions, they differ in absolute performance magnitude. Additionally, overall academic capability accounts for over 99% of total score variance, while supervised LDA projection provides a clean classification boundary for passing and failing thresholds.

Overall, the project demonstrates how Linear Algebra methods can transform multidimensional student records into visualizable, mathematically sound student profiles to support informed academic evaluations.

---

### 👤 Priyansh Vekariya

*   📍 Ahmedabad, Gujarat, India
*   ⭐ If you found this project helpful, give it a star and feel free to fork!
*   📐 **Linear Algebra · Dimensionality Reduction · Matrix Decompositions**

