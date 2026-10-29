from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ─── COLOUR PALETTE ────────────────────────────────────────────
NAVY      = HexColor("#1a237e")   # deep blue – title/headers
TEAL      = HexColor("#00695c")   # dark teal – section headings
ACCENT    = HexColor("#e65100")   # orange – question boxes
SOFT_BLUE = HexColor("#e8eaf6")   # light indigo – section bg
SOFT_GRN  = HexColor("#e8f5e9")   # light green – example boxes
SOFT_ORG  = HexColor("#fff3e0")   # light orange – note boxes
SOFT_GREY = HexColor("#f5f5f5")   # table alternating rows
SOFT_TEAL = HexColor("#e0f2f1")   # formula boxes
MID_GREY  = HexColor("#bdbdbd")

# ─── DOCUMENT SETUP ────────────────────────────────────────────
doc = SimpleDocTemplate(
    "ML_Theory_Notes.pdf",
    pagesize=A4,
    leftMargin=1.8*cm, rightMargin=1.8*cm,
    topMargin=2.0*cm,  bottomMargin=2.0*cm,
)
W = A4[0] - 3.6*cm   # usable width

# ─── STYLE SHEET ───────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    """Build a ParagraphStyle quickly."""
    return ParagraphStyle(name, **kw)

TITLE  = S("TITLE",  fontName="Helvetica-Bold", fontSize=22,
           textColor=white,  alignment=TA_CENTER, spaceAfter=6)
SUB    = S("SUB",    fontName="Helvetica",       fontSize=11,
           textColor=HexColor("#e8eaf6"), alignment=TA_CENTER)
QTAG   = S("QTAG",   fontName="Helvetica-Bold",  fontSize=12,
           textColor=white,  alignment=TA_LEFT)
QTEXT  = S("QTEXT",  fontName="Helvetica-Bold",  fontSize=12,
           textColor=NAVY,   alignment=TA_LEFT, spaceAfter=4)
H1     = S("H1",     fontName="Helvetica-Bold",  fontSize=13,
           textColor=TEAL,   spaceBefore=6, spaceAfter=3)
H2     = S("H2",     fontName="Helvetica-Bold",  fontSize=11,
           textColor=NAVY,   spaceBefore=4, spaceAfter=2)
BODY   = S("BODY",   fontName="Helvetica",       fontSize=10,
           textColor=HexColor("#212121"), leading=15,
           alignment=TA_JUSTIFY, spaceAfter=3)
BULLET = S("BULLET", fontName="Helvetica",       fontSize=10,
           textColor=HexColor("#212121"), leading=15,
           leftIndent=14, spaceAfter=2,
           bulletIndent=4, alignment=TA_LEFT)
CODE   = S("CODE",   fontName="Courier",         fontSize=9.5,
           textColor=HexColor("#1b5e20"), leading=14,
           leftIndent=10, spaceAfter=2)
FORMULA= S("FORMULA",fontName="Courier-Bold",    fontSize=10,
           textColor=NAVY, alignment=TA_CENTER, leading=16)
NOTE   = S("NOTE",   fontName="Helvetica-Oblique", fontSize=9.5,
           textColor=HexColor("#4e342e"), leading=14, spaceAfter=2)
FOOTER = S("FOOTER", fontName="Helvetica-Oblique", fontSize=8,
           textColor=HexColor("#757575"), alignment=TA_CENTER)
DEFH   = S("DEFH",   fontName="Helvetica-Bold",  fontSize=10,
           textColor=NAVY, spaceAfter=2)

# ─── HELPER BUILDERS ───────────────────────────────────────────
def title_block(story):
    data = [[Paragraph("Machine Learning — Core Theory Notes", TITLE)],
            [Paragraph("Regression | Classification | Regularisation | Metrics | Cross-Validation", SUB)]]
    t = Table(data, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("ROUNDEDCORNERS", [8]),
        ("TOPPADDING",    (0,0), (-1,-1), 16),
        ("BOTTOMPADDING", (0,0), (-1,-1), 16),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.35*cm))


def section_header(story, num, text):
    """Numbered section header with coloured background."""
    data = [[Paragraph(f"Q{num}   {text}", QTAG)]]
    t = Table(data, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), ACCENT),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS",[5]),
    ]))
    story.append(KeepTogether([t, Spacer(1, 0.15*cm)]))


def coloured_box(story, paragraphs, bg=SOFT_BLUE, pad=8):
    data = [[p] for p in paragraphs]
    t = Table(data, colWidths=[W - 0.3*cm])
    style = [
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (0,0),   pad),
        ("BOTTOMPADDING", (0,-1),(-1,-1), pad),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ]
    t.setStyle(TableStyle(style))
    story.append(t)
    story.append(Spacer(1, 0.2*cm))


def two_col_table(story, headers, rows, col_widths=None):
    if col_widths is None:
        col_widths = [W * 0.33, W * 0.33, W * 0.34]
    hdr_style = ParagraphStyle("th", fontName="Helvetica-Bold",
                               fontSize=10, textColor=white, alignment=TA_CENTER)
    cell_style = ParagraphStyle("td", fontName="Helvetica", fontSize=9.5,
                                leading=13, alignment=TA_LEFT)
    table_data = [[Paragraph(h, hdr_style) for h in headers]]
    for row in rows:
        table_data.append([Paragraph(str(c), cell_style) for c in row])

    ts = TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  TEAL),
        ("TEXTCOLOR",     (0,0), (-1,0),  white),
        ("GRID",          (0,0), (-1,-1), 0.4, MID_GREY),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ])
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            ts.add("BACKGROUND", (0,i), (-1,i), SOFT_GREY)
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(ts)
    story.append(t)
    story.append(Spacer(1, 0.2*cm))


def formula_box(story, lines):
    items = [Paragraph(l, FORMULA) for l in lines]
    coloured_box(story, items, bg=SOFT_TEAL)


def hr(story):
    story.append(HRFlowable(width=W, thickness=0.5,
                            color=MID_GREY, spaceAfter=6, spaceBefore=6))


def bp(text):
    return Paragraph(f"\u2022  {text}", BULLET)


def p(text, style=BODY):
    return Paragraph(text, style)

# ═══════════════════════════════════════════════════════════════
story = []

title_block(story)

# ───────────────────────────────────────────────────────────────
# Q1 – Regression vs Classification
# ───────────────────────────────────────────────────────────────
section_header(story, 1,
    "What is Regression? How is it different from Classification?")

story.extend([
    p("<b>Definition of Regression:</b>", H1),
    p("Regression is a supervised machine learning technique used to predict a <b>continuous numerical output</b> (a real-valued quantity). The model learns a mathematical mapping from input features X to a continuous target variable y by minimising a loss function — typically Mean Squared Error (MSE)."),
    Spacer(1, 0.15*cm),
])

formula_box(story, [
    "Goal:  learn  f(X)  such that  y_hat = f(X)  minimises  MSE = (1/n) * SUM[ (y_i - y_hat_i)^2 ]"
])

story.extend([
    p("<b>Definition of Classification:</b>", H1),
    p("Classification predicts a <b>discrete class label</b> (a category) from a finite set. The model learns decision boundaries that separate data points into distinct groups. Loss is typically Cross-Entropy."),
    Spacer(1, 0.15*cm),
])

coloured_box(story, [
    p("<b>Key Distinction at a Glance:</b>", H2),
    p("• <b>Regression</b>  →  Output is a NUMBER  (salary, temperature, house price)"),
    p("• <b>Classification</b>  →  Output is a CATEGORY  (spam/not spam, disease/healthy)"),
], bg=SOFT_BLUE)

story.append(p("<b>Comparison Table:</b>", H1))

two_col_table(story,
    ["Aspect", "Regression", "Classification"],
    [
        ["Output Type",     "Continuous number",                   "Discrete class label"],
        ["Example Output",  "₹68,40,000 property price",           "APPROVED / REJECTED"],
        ["Loss Function",   "MSE / RMSE / MAE",                    "Cross-Entropy / Log Loss"],
        ["Evaluation",      "R², RMSE, MAE",                       "Accuracy, Precision, Recall, F1"],
        ["Decision Boundary","No fixed boundary — learns a curve",  "Learns a separating hyperplane"],
        ["Algorithms",      "Linear Reg., Ridge, XGBoost Reg.",     "Logistic Reg., SVM, RF Classifier"],
    ],
    col_widths=[W*0.22, W*0.39, W*0.39]
)

story.extend([
    p("<b>Real-World Indian Examples:</b>", H1),
])

coloured_box(story, [
    p("<b>Example 1 — HDFC Bank: EMI Amount Prediction (Regression)</b>", DEFH),
    p("HDFC's home loan engine collects applicant features — monthly income, CIBIL credit score, loan tenor, property valuation, LTV ratio — and predicts the exact monthly EMI (a continuous number in ₹). Since EMI can be ₹12,500 or ₹87,430.50, this is a regression problem where the model minimises prediction error on a continuous scale."),
    Spacer(1, 0.1*cm),
    p("<b>Features (X):</b>  Monthly Income, CIBIL Score, Loan Amount, Tenor, Age"),
    p("<b>Target (y):</b>  EMI in ₹  (e.g., ₹24,350.75/month)"),
], bg=SOFT_GRN)

story.append(Spacer(1, 0.15*cm))

coloured_box(story, [
    p("<b>Example 2 — Maharashtra Agriculture: Crop Yield Prediction (Regression)</b>", DEFH),
    p("The Maharashtra Government and ICAR use satellite remote-sensing data, soil health cards, rainfall records, and fertiliser usage to predict wheat/soybean yield in quintals/hectare for Vidarbha and Marathwada farmers. This continuous output guides MSP (Minimum Support Price) procurement and mandi supply planning."),
    Spacer(1, 0.1*cm),
    p("<b>Features (X):</b>  Rainfall (mm), Soil NPK, Temperature, Sowing Date, Crop Variety"),
    p("<b>Target (y):</b>  Yield in quintals/hectare  (e.g., 18.6 q/ha)"),
], bg=SOFT_GRN)

coloured_box(story, [
    p("<b>Counter-example (Classification):</b>  SBI's loan default detection. Here the output is binary — DEFAULT (1) or NO DEFAULT (0) — so Classification models like Logistic Regression or XGBoost Classifier are used, not regression.", NOTE),
], bg=SOFT_ORG)

hr(story)

# ───────────────────────────────────────────────────────────────
# Q2 – SLR vs MLR vs Regularised Regression
# ───────────────────────────────────────────────────────────────
section_header(story, 2,
    "Simple Linear Regression vs Multiple Linear Regression vs Regularised Regression")

story.extend([
    p("<b>Simple Linear Regression (SLR):</b>", H1),
    p("Models the linear relationship between <b>one independent variable (feature)</b> and one dependent variable (target). It finds the best-fit straight line through the data."),
])

formula_box(story, [
    "y = beta_0  +  beta_1 * X  +  epsilon",
    "Where:  beta_0 = intercept,   beta_1 = slope,   epsilon = error term",
])

coloured_box(story, [
    p("<b>Example:</b>  Predicting a student's exam marks (y) purely based on hours studied (X)."),
    p("<b>Limitation:</b>  Real-world outcomes rarely depend on just one variable.", NOTE),
], bg=SOFT_GRN)

story.extend([
    Spacer(1, 0.15*cm),
    p("<b>Multiple Linear Regression (MLR):</b>", H1),
    p("Extends SLR to <b>two or more independent variables</b>. The model fits a hyperplane (multi-dimensional surface) through the data points."),
])

formula_box(story, [
    "y = beta_0  +  beta_1*X_1  +  beta_2*X_2  +  ...  +  beta_p*X_p  +  epsilon",
    "Example:  SalePrice = b0 + b1*GrLivArea + b2*OverallQual + b3*YearBuilt + ...",
])

coloured_box(story, [
    p("<b>Example:</b>  HDFC property valuation model — SalePrice predicted using 79 features (area, quality, age, garage, neighbourhood etc.) — exactly the Ames Housing problem."),
    p("<b>Problem:</b>  When features are many (p >> n) or strongly correlated (multicollinearity), OLS coefficient estimates become <b>unstable and blow up</b> — overfitting occurs.", NOTE),
], bg=SOFT_GRN)

story.extend([
    Spacer(1, 0.15*cm),
    p("<b>Regularised Regression (Ridge &amp; Lasso):</b>", H1),
    p("Regularisation adds a <b>penalty term</b> to the OLS loss function that shrinks large coefficients toward zero. This reduces variance (overfitting) at the cost of a small increase in bias — the classic Bias-Variance Trade-off."),
])

formula_box(story, [
    "Ridge  Loss  =  SUM[(y_i - y_hat_i)^2]  +  lambda * SUM[ beta_j^2 ]   (L2 penalty)",
    "Lasso  Loss  =  SUM[(y_i - y_hat_i)^2]  +  lambda * SUM[ |beta_j| ]   (L1 penalty)",
])

two_col_table(story,
    ["Property", "Ridge (L2)", "Lasso (L1)"],
    [
        ["Penalty",            "Square of coefficients (L2 norm)",  "Absolute value of coefficients (L1 norm)"],
        ["Coefficient Behaviour","Shrinks all toward zero; none become exactly 0", "Can force some to exactly 0 (feature selection)"],
        ["Sparsity",           "Dense — all features retained",     "Sparse — irrelevant features eliminated"],
        ["Best For",           "Multicollinearity; many small effects", "High-dimensional data; automatic feature selection"],
        ["Alpha Tuning",       "RidgeCV auto-selects optimal alpha", "LassoCV auto-selects optimal alpha"],
        ["Our Project Result", "RMSE $20,497 (alpha=10)",           "RMSE $20,058 (alpha=0.001, 123 features zeroed)"],
    ],
    col_widths=[W*0.22, W*0.39, W*0.39]
)

coloured_box(story, [
    p("<b>Key Insight:</b>  When lambda = 0, regularised regression reduces to plain OLS. As lambda increases, model coefficients shrink more aggressively, trading lower variance for higher bias.", NOTE),
], bg=SOFT_ORG)

hr(story)

# ───────────────────────────────────────────────────────────────
# Q3 – Overfitting & Underfitting
# ───────────────────────────────────────────────────────────────
section_header(story, 3,
    "Explain Overfitting and Underfitting. How does Regularisation (L1/L2) help?")

story.extend([
    p("<b>Underfitting (High Bias):</b>", H1),
    p("The model is too simple to capture the true relationship in the data. It performs poorly on <b>both training and test sets</b>. Analogously — a student who did not study enough fails both mock exams and the final."),
])

two_col_table(story,
    ["Characteristic", "Underfitting", "Overfitting"],
    [
        ["Also Called",    "High Bias Model",          "High Variance Model"],
        ["Training Error", "HIGH",                      "Very LOW (memorises data)"],
        ["Test Error",     "HIGH",                      "HIGH (fails to generalise)"],
        ["Root Cause",     "Model too simple / few features", "Model too complex / too many features"],
        ["Visual Sign",    "Flat/straight line through curved data", "Wiggly curve that passes through every data point"],
        ["Fix",            "More features, higher-order terms, more complex model", "Regularisation, more data, cross-validation, dropout"],
    ],
    col_widths=[W*0.22, W*0.39, W*0.39]
)

story.extend([
    p("<b>Overfitting (High Variance):</b>", H1),
    p("The model memorises training data noise and random fluctuations instead of learning the true underlying pattern. It performs <b>excellently on training data but poorly on unseen test data</b>. Like a student who mugged only previous year questions — helpless when a new question pattern appears in the final exam."),
    Spacer(1, 0.15*cm),
    p("<b>The Bias-Variance Trade-Off:</b>", H1),
])

formula_box(story, [
    "Total Error  =  Bias^2  +  Variance  +  Irreducible Noise",
    "Goal:  minimise BOTH bias AND variance simultaneously",
])

story.extend([
    Spacer(1, 0.15*cm),
    p("<b>How L1 (Lasso) and L2 (Ridge) Regularisation Help:</b>", H1),
])

coloured_box(story, [
    p("<b>Mechanism:</b>  Regularisation modifies the objective function by adding a penalty on coefficient magnitudes. This forces the optimiser to keep weights small, preventing the model from fitting noise."),
    Spacer(1, 0.1*cm),
    p("<b>Ridge (L2):</b>  Penalises large squared coefficients → spreads weight evenly across correlated features → reduces coefficient instability without eliminating any feature."),
    p("<b>Lasso (L1):</b>  Penalises absolute values → geometrically, the L1 ball has corners on the axes, so the optimal solution often lands exactly on an axis (coefficient = 0) → automatic feature selection."),
    Spacer(1, 0.1*cm),
    p("<b>Lambda (alpha) Effect:</b>", DEFH),
    p("  • lambda = 0   →   Plain OLS regression  (may overfit)"),
    p("  • lambda = small   →   Mild regularisation  (sweet spot)"),
    p("  • lambda = large   →   All coefficients → 0  (underfitting)"),
    p("  • Optimal lambda found via Cross-Validation (RidgeCV / LassoCV)"),
], bg=SOFT_BLUE)

coloured_box(story, [
    p("<b>Our Project Evidence:</b>  Plain Linear Regression (no regularisation) achieved RMSE = $22,630 on the Ames Housing test set. Adding Ridge regularisation improved RMSE to $20,497. Lasso further improved to $20,058 by pruning 123 redundant features.", NOTE),
], bg=SOFT_ORG)

hr(story)

# ───────────────────────────────────────────────────────────────
# Q4 – RMSE, MAE, R²
# ───────────────────────────────────────────────────────────────
section_header(story, 4,
    "Define RMSE, MAE, and R². When would you prefer RMSE over MAE?")

story.append(p("<b>Mean Absolute Error (MAE):</b>", H1))
formula_box(story, [
    "MAE  =  (1/n)  *  SUM[ |y_i  -  y_hat_i| ]",
])
coloured_box(story, [
    p("• Measures the <b>average absolute deviation</b> between actual and predicted values."),
    p("• <b>Robust to outliers</b> — each error contributes equally regardless of its magnitude."),
    p("• Interpretable in original units (e.g., 'on average predictions are off by ₹14,162')."),
    p("• Gradient is constant → can cause oscillation near the minimum during gradient descent."),
], bg=SOFT_BLUE)

story.append(Spacer(1, 0.1*cm))
story.append(p("<b>Root Mean Squared Error (RMSE):</b>", H1))
formula_box(story, [
    "RMSE  =  SQRT[ (1/n)  *  SUM[ (y_i  -  y_hat_i)^2 ] ]",
])
coloured_box(story, [
    p("• <b>Squares errors</b> before averaging, then takes the square root → larger errors are penalised more heavily than smaller ones."),
    p("• Sensitive to outliers and large deviations."),
    p("• Also interpretable in original units (same scale as y)."),
    p("• RMSE >= MAE always. When RMSE >> MAE, large outlier errors are present in the predictions."),
], bg=SOFT_BLUE)

story.append(Spacer(1, 0.1*cm))
story.append(p("<b>R-Squared (Coefficient of Determination, R²):</b>", H1))
formula_box(story, [
    "R^2  =  1  -  [ SUM(y_i - y_hat_i)^2  /  SUM(y_i - y_mean)^2 ]",
    "Interpretation:  R^2 = 0.93  means model explains 93% of variance in SalePrice",
])
coloured_box(story, [
    p("• <b>Scale-free</b> measure between 0 and 1 (can be negative for very poor models)."),
    p("• R² = 1.0 → perfect predictions. R² = 0 → model is no better than predicting the mean."),
    p("• Does not penalise for model complexity → use Adjusted R² when comparing models with different number of features."),
], bg=SOFT_BLUE)

story.append(p("<b>RMSE vs MAE — When to Prefer Which?</b>", H1))
two_col_table(story,
    ["Scenario", "Preferred Metric", "Reason"],
    [
        ["Large outliers are rare but critical\n(e.g., house price errors of ₹50L are very costly)",
         "RMSE",
         "Squares the error → heavily penalises large deviations, forcing the model to minimise costly mistakes"],
        ["Outliers are common / data is noisy\n(e.g., noisy IoT sensor readings)",
         "MAE",
         "Treats all errors equally; outliers don't dominate the metric"],
        ["Business cost of large errors is disproportionately high\n(e.g., HDFC loan defaults: ₹1Cr error >> ₹1L error)",
         "RMSE",
         "Quadratic penalty aligns metric with asymmetric real-world cost"],
        ["Median prediction is more meaningful than mean\n(e.g., income distribution skew)",
         "MAE",
         "MAE corresponds to median-optimal prediction; RMSE to mean-optimal prediction"],
        ["Comparing across models (same dataset)",
         "Both",
         "RMSE for sensitivity to large errors; MAE for robust overall performance view"],
    ],
    col_widths=[W*0.36, W*0.18, W*0.46]
)

coloured_box(story, [
    p("<b>PropTech / NoBroker Context:</b>  RMSE is preferred for property price prediction because a ₹50 lakh over-valuation is catastrophically worse than a ₹5 lakh error for a home buyer taking a 20-year mortgage. RMSE's squared penalty forces the model to avoid such extreme misvaluations.", NOTE),
], bg=SOFT_ORG)

hr(story)

# ───────────────────────────────────────────────────────────────
# Q5 – Cross-Validation
# ───────────────────────────────────────────────────────────────
section_header(story, 5,
    "What is Cross-Validation (k-Fold)? Why preferred over single train-test split?")

story.extend([
    p("<b>What is Cross-Validation?</b>", H1),
    p("Cross-Validation (CV) is a <b>statistical resampling technique</b> that evaluates how well a machine learning model generalises to an independent (unseen) dataset. Instead of relying on a single arbitrary train-test split, CV systematically rotates the holdout set to get a robust, low-variance estimate of model performance."),
    Spacer(1, 0.15*cm),
    p("<b>k-Fold Cross-Validation — Step-by-Step:</b>", H1),
])

coloured_box(story, [
    p("<b>Step 1:</b>  Shuffle the dataset randomly."),
    p("<b>Step 2:</b>  Divide the dataset into k equal-sized folds (subsets). Typical k = 5 or 10."),
    p("<b>Step 3:</b>  Repeat k times:  Use fold i as the Validation set. Train the model on the remaining k-1 folds.  Record the validation score (e.g., RMSE)."),
    p("<b>Step 4:</b>  Final CV Score  =  Mean of all k validation scores  ±  Std Dev."),
    Spacer(1, 0.1*cm),
    p("<b>For k = 5 folds:</b>", DEFH),
    p("  Fold 1: [TEST][train][train][train][train]"),
    p("  Fold 2: [train][TEST][train][train][train]"),
    p("  Fold 3: [train][train][TEST][train][train]"),
    p("  Fold 4: [train][train][train][TEST][train]"),
    p("  Fold 5: [train][train][train][train][TEST]"),
    p("  ─────────────────────────────────────────"),
    p("  CV RMSE  =  Mean(RMSE_1, RMSE_2, RMSE_3, RMSE_4, RMSE_5)"),
], bg=SOFT_TEAL)

story.extend([
    Spacer(1, 0.15*cm),
    p("<b>Why Preferred Over a Single Train-Test Split?</b>", H1),
])

two_col_table(story,
    ["Issue", "Single Train-Test Split", "k-Fold Cross-Validation"],
    [
        ["Data Efficiency",
         "Only 1 subset used for evaluation. 20% data wasted for testing and never used for training.",
         "Every data point is used for both training AND validation across different folds. Maximum data utilisation."],
        ["Variance / Reliability",
         "Score heavily depends on which rows ended up in test set (luck of the split). High variance.",
         "Averages over k independent evaluations. Low variance, statistically robust score."],
        ["Overfitting Detection",
         "Easy to get a lucky split where test set happens to be easy. May give falsely optimistic results.",
         "Harder to overfit to k different validation sets simultaneously. Better true generalisation estimate."],
        ["Hyperparameter Tuning",
         "If you tune hyperparameters to one split, model overfits to that test set (data leakage).",
         "CV provides an uncontaminated evaluation for hyperparameter selection (RandomizedSearchCV)."],
        ["Small Datasets",
         "Losing 20% of data to test set is very costly when data is scarce.",
         "k-Fold makes full use of limited data — critical for medical/agricultural datasets."],
        ["Reproducibility",
         "Results change with random seed.",
         "With shuffle=True and random_state fixed, results are reproducible and stable."],
    ],
    col_widths=[W*0.20, W*0.37, W*0.43]
)

coloured_box(story, [
    p("<b>Choosing k:</b>", DEFH),
    p("• <b>k = 5 or 10</b>  →  Standard. Good balance of bias vs variance in the estimate."),
    p("• <b>k = n (Leave-One-Out CV)</b>  →  Maximum data use but computationally expensive; high variance."),
    p("• <b>Stratified k-Fold</b>  →  Used in classification to maintain class distribution in each fold."),
], bg=SOFT_BLUE)

coloured_box(story, [
    p("<b>Our Project (Ames Housing):</b>  We used 5-Fold CV on the tuned XGBoost model. CV Log RMSE = 0.1197 ± small std. This aligned closely with the holdout test RMSE ($19,636), confirming that the model generalises well and is not overfitting to the 80% training set.", NOTE),
], bg=SOFT_ORG)

# ─── SUMMARY TABLE ─────────────────────────────────────────────
story.append(Spacer(1, 0.2*cm))
story.append(p("<b>Quick Reference Summary — All 5 Topics</b>", H1))
two_col_table(story,
    ["Topic", "Core Idea", "Key Formula / Rule of Thumb"],
    [
        ["Regression vs Classification",
         "Regression → continuous output. Classification → discrete label.",
         "If output is a number → Regression. If output is a class → Classification."],
        ["SLR vs MLR vs Regularised",
         "SLR: 1 feature. MLR: multiple features. Regularised: adds penalty to control complexity.",
         "Ridge: L2 penalty (all coef shrunk). Lasso: L1 penalty (some coef → 0)."],
        ["Overfitting vs Underfitting",
         "Overfitting: low train error, high test error. Underfitting: high error on both.",
         "Total Error = Bias² + Variance + Noise. Balance via regularisation + CV."],
        ["RMSE vs MAE vs R²",
         "RMSE penalises large errors more. MAE treats all errors equally. R² measures explained variance.",
         "RMSE ≥ MAE always. R² = 1 → perfect. Prefer RMSE when large errors are costly."],
        ["Cross-Validation",
         "Rotate holdout fold k times. Average k scores for robust evaluation.",
         "k=5 or k=10 standard. CV Score = Mean ± Std of k validation scores."],
    ],
    col_widths=[W*0.20, W*0.42, W*0.38]
)

# ─── FOOTER ────────────────────────────────────────────────────
story.extend([
    Spacer(1, 0.4*cm),
    HRFlowable(width=W, thickness=1, color=NAVY),
    Spacer(1, 0.15*cm),
    Paragraph(
        "ML Theory Notes  |  Supervised Learning — Regression Deep Dive  |  Prepared for Final Examination",
        FOOTER),
])

# ─── BUILD PDF ─────────────────────────────────────────────────
doc.build(story)
print("PDF generated successfully: ML_Theory_Notes.pdf")

