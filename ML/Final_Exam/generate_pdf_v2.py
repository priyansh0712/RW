"""
ML Theory Notes — Beautiful PDF with full Unicode support
Uses Calibri (Windows system font) for proper rendering of Greek/math symbols.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Register Unicode-capable Calibri family ────────────────────
pdfmetrics.registerFont(TTFont('Cal',    'C:/Windows/Fonts/calibri.ttf'))
pdfmetrics.registerFont(TTFont('CalB',   'C:/Windows/Fonts/calibrib.ttf'))
pdfmetrics.registerFont(TTFont('CalI',   'C:/Windows/Fonts/calibrii.ttf'))
pdfmetrics.registerFont(TTFont('CalBI',  'C:/Windows/Fonts/calibriz.ttf'))
pdfmetrics.registerFont(TTFont('GeorgB', 'C:/Windows/Fonts/georgiab.ttf'))
pdfmetrics.registerFontFamily('Calibri', normal='Cal', bold='CalB',
                               italic='CalI', boldItalic='CalBI')

# ── Colour Palette ─────────────────────────────────────────────
NAVY      = HexColor("#1C2B4B")   # deep navy blue  – headers
TEAL      = HexColor("#006D5B")   # dark teal       – subheadings
ORANGE    = HexColor("#D4500A")   # burnt orange    – question tags
GOLD      = HexColor("#B8860B")   # dark gold       – accents
SOFTBLUE  = HexColor("#EAF2FB")   # light blue      – theory boxes
SOFTGREEN = HexColor("#E9F7EF")   # light green     – example boxes
SOFTORANGE= HexColor("#FEF9E7")   # cream orange    – note boxes
SOFTTEAL  = HexColor("#E8F6F3")   # light teal      – formula boxes
SOFTPURP  = HexColor("#F4ECF7")   # lavender        – definition boxes
MIDGREY   = HexColor("#C8CDD5")
DARKTEXT  = HexColor("#1A1A2E")
SUBTEXT   = HexColor("#4A4A6A")
ROWALT    = HexColor("#F2F5F9")
HEADBG    = HexColor("#1C2B4B")

W, H = A4
MARGIN = 1.7 * cm
USABLE = W - 2 * MARGIN

# ── Style Factory ─────────────────────────────────────────────
def sty(name, font='Cal', size=10.5, color=DARKTEXT,
        align=TA_LEFT, leading=None, **kw):
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        textColor=color,
        alignment=align,
        leading=leading or size * 1.45,
        **kw
    )

# All named styles
S = {
    'cover_title': sty('ct',  'GeorgB', 26, white,    TA_CENTER, spaceAfter=4),
    'cover_sub':   sty('cs',  'CalI',   12, HexColor("#C8DCF5"), TA_CENTER),
    'cover_tag':   sty('ctg', 'CalB',   10, HexColor("#90BDE0"), TA_CENTER),

    'q_num':   sty('qn', 'CalB', 12, white, TA_LEFT),
    'q_text':  sty('qt', 'CalB', 12, NAVY,  TA_LEFT, spaceAfter=3),

    'h1':  sty('h1', 'CalB', 12, TEAL,  spaceBefore=6, spaceAfter=3),
    'h2':  sty('h2', 'CalB', 11, NAVY,  spaceBefore=4, spaceAfter=2),
    'h3':  sty('h3', 'CalB', 10.5, ORANGE, spaceBefore=3, spaceAfter=1),

    'body':   sty('bd',  'Cal',  10.5, DARKTEXT, TA_JUSTIFY, leading=16.5, spaceAfter=3),
    'bodyL':  sty('bdl', 'Cal',  10.5, DARKTEXT, TA_LEFT,    leading=16.5, spaceAfter=2),
    'bullet': sty('bl',  'Cal',  10.5, DARKTEXT, TA_LEFT,    leading=16,
                  leftIndent=16, spaceAfter=2),
    'subbul': sty('sb',  'Cal',  10,   SUBTEXT,  TA_LEFT,    leading=15,
                  leftIndent=32, spaceAfter=1),

    'formula': sty('fm',  'CalB', 11,   NAVY,    TA_CENTER, leading=18),
    'fmsmall': sty('fms', 'Cal',  10,   TEAL,    TA_CENTER, leading=15),
    'code':    sty('cd',  'CalB', 10,   HexColor("#1A5276"), TA_LEFT, leading=16,
                   leftIndent=8),

    'note':    sty('nt', 'CalI', 10,   HexColor("#6E2F0A"), TA_JUSTIFY, leading=14, spaceAfter=2),
    'defh':    sty('dh', 'CalB', 10.5, NAVY,   spaceAfter=2),

    'th':  sty('th', 'CalB', 9.5, white,    TA_CENTER, leading=13),
    'td':  sty('td', 'Cal',  9.5, DARKTEXT, TA_LEFT,   leading=13.5),
    'tdc': sty('tc', 'Cal',  9.5, DARKTEXT, TA_CENTER, leading=13.5),

    'footer': sty('ft', 'CalI', 8.5, HexColor("#7F8C8D"), TA_CENTER),
    'pg':     sty('pg', 'CalB', 9,   white,  TA_RIGHT),
}

# ── Helper builders ────────────────────────────────────────────
def P(text, style='body'):
    return Paragraph(text, S[style] if isinstance(style, str) else style)

def BP(text, indent=0):
    """Bullet paragraph with Unicode bullet."""
    st = sty(f'bp{indent}', 'Cal', 10.5, DARKTEXT, TA_LEFT, leading=16,
             leftIndent=16 + indent*16, spaceAfter=2)
    marker = '\u2022' if indent == 0 else '\u25E6'
    return Paragraph(f'{marker}\u2002 {text}', st)

def SP(h=0.2):
    return Spacer(1, h * cm)

def HR(color=MIDGREY, thickness=0.5):
    return HRFlowable(width=USABLE, thickness=thickness, color=color,
                      spaceAfter=5, spaceBefore=5)


def section_tag(num, text):
    """Coloured question header box."""
    inner = [
        [P(f'\u2756  Question {num}', 'q_num'),
         P(text, S['q_num'])],
    ]
    tag = Table([[P(f'\u2756  Q{num}   \u2014   {text}', 'q_num')]],
                colWidths=[USABLE])
    tag.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), ORANGE),
        ('TOPPADDING',    (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
        ('LEFTPADDING',   (0,0), (-1,-1), 14),
        ('RIGHTPADDING',  (0,0), (-1,-1), 14),
        ('ROUNDEDCORNERS', [6]),
    ]))
    return tag


def colbox(items, bg=SOFTBLUE, lpad=10, rpad=10, tpad=8, bpad=8):
    """Coloured box containing a list of flowables (Paragraphs)."""
    rows = [[item] for item in items]
    t = Table(rows, colWidths=[USABLE - 0.6*cm])
    style = [
        ('BACKGROUND',    (0,0),  (-1,-1), bg),
        ('LEFTPADDING',   (0,0),  (-1,-1), lpad),
        ('RIGHTPADDING',  (0,0),  (-1,-1), rpad),
        ('TOPPADDING',    (0,0),  (0,0),   tpad),
        ('BOTTOMPADDING', (0,-1), (-1,-1), bpad),
        ('TOPPADDING',    (0,1),  (-1,-1), 3),
        ('BOTTOMPADDING', (0,0),  (-1,-2), 1),
    ]
    t.setStyle(TableStyle(style))
    return t


def formula_box(*lines):
    items = []
    for i, l in enumerate(lines):
        st = 'formula' if i == 0 else 'fmsmall'
        items.append(P(l, st))
    return colbox(items, bg=SOFTTEAL, tpad=10, bpad=10)


def comparison_table(headers, rows, col_widths=None):
    if col_widths is None:
        n = len(headers)
        col_widths = [USABLE / n] * n

    hrow = [P(h, 'th') for h in headers]
    data = [hrow]
    for row in rows:
        data.append([P(str(c), 'td') for c in row])

    ts = TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  HEADBG),
        ('TEXTCOLOR',     (0,0), (-1,0),  white),
        ('GRID',          (0,0), (-1,-1), 0.35, MIDGREY),
        ('TOPPADDING',    (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('RIGHTPADDING',  (0,0), (-1,-1), 8),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW',     (0,0), (-1,0),  1.2, TEAL),
    ])
    for i in range(1, len(data)):
        if i % 2 == 0:
            ts.add('BACKGROUND', (0,i), (-1,i), ROWALT)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(ts)
    return t


def step_box(steps):
    """Numbered steps in a styled box."""
    items = [P('\u27A4  Step-by-Step Process:', 'h2')]
    for i, s in enumerate(steps, 1):
        items.append(P(f'  <b>Step {i}:</b>  {s}', 'bodyL'))
    return colbox(items, bg=SOFTBLUE)


# ══════════════════════════════════════════════════════════════
#  CONTENT BUILDER
# ══════════════════════════════════════════════════════════════
story = []

# ─────────────────────────────────────────────────────────────
#  COVER PAGE
# ─────────────────────────────────────────────────────────────
story.append(SP(3.5))

cover_title_data = [[
    P('Machine Learning', 'cover_title'),
]]
ct = Table(cover_title_data, colWidths=[USABLE])
ct.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,-1), NAVY),
    ('TOPPADDING',    (0,0), (-1,-1), 24),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING',   (0,0), (-1,-1), 20),
    ('RIGHTPADDING',  (0,0), (-1,-1), 20),
]))
story.append(ct)

cover_sub_data = [[P('Core Theory Notes', 'cover_sub')]]
cs = Table(cover_sub_data, colWidths=[USABLE])
cs.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,-1), NAVY),
    ('TOPPADDING',    (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ('LEFTPADDING',   (0,0), (-1,-1), 20),
    ('RIGHTPADDING',  (0,0), (-1,-1), 20),
]))
story.append(cs)

story.append(SP(0.6))

# Topic pills row
topics = [
    '\u2460  Regression vs Classification',
    '\u2461  Linear vs Regularised',
    '\u2462  Overfitting & Underfitting',
    '\u2463  RMSE, MAE & R\u00b2',
    '\u2464  Cross-Validation',
]
for t in topics:
    row = [[P(t, sty('pill','CalB',10.5,white,TA_CENTER))]]
    pill = Table(row, colWidths=[USABLE])
    pill.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), TEAL),
        ('TOPPADDING',    (0,0),(-1,-1), 7),
        ('BOTTOMPADDING', (0,0),(-1,-1), 7),
        ('LEFTPADDING',   (0,0),(-1,-1), 15),
        ('RIGHTPADDING',  (0,0),(-1,-1), 15),
        ('ROUNDEDCORNERS',[5]),
    ]))
    story.append(pill)
    story.append(SP(0.18))

story.append(SP(1.2))
story.append(HR(NAVY, 1.5))
story.append(SP(0.3))
story.append(P('Supervised Learning \u2014 Regression Deep Dive  \u2022  Final Examination Preparation', 'footer'))
story.append(P('Ames Housing Project \u2014 PropTech Valuation Context (NoBroker / MagicBricks)', 'footer'))

story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
#  Q1  Regression vs Classification
# ─────────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_tag(1, 'What is Regression? How is it different from Classification?'),
    SP(0.25),
]))

story.append(P('\U0001F4D6  Definition of Regression', 'h1'))
story.append(P(
    'Regression is a <b>supervised machine learning technique</b> used to predict a '
    '<b>continuous numerical output</b> (a real-valued quantity). The model learns a '
    'mapping f(X) \u2192 \u0177 by minimising a loss function (typically Mean Squared Error) '
    'on labelled training examples.',
    'body'))

story.append(formula_box(
    'Objective:   minimise   MSE = \u00b9\u2215\u2099 \u00d7 \u03a3(y\u1d62 \u2212 \u0177\u1d62)\u00b2',
    'where  y\u1d62 = actual value,   \u0177\u1d62 = predicted value,   n = number of samples'
))
story.append(SP(0.25))

story.append(P('\U0001F4D6  Definition of Classification', 'h1'))
story.append(P(
    'Classification predicts a <b>discrete class label</b> from a finite set of categories. '
    'The model learns decision boundaries that separate data points into distinct groups, '
    'minimising a classification loss (typically Cross-Entropy).',
    'body'))
story.append(SP(0.15))

story.append(colbox([
    P('\u2728  The Core Distinction', 'h2'),
    SP(0.05),
    P('\u2022\u2002 <b>Regression</b> \u2192 Output is a <b>NUMBER</b> &nbsp;&nbsp;(salary, temperature, property price, crop yield)', 'bodyL'),
    P('\u2022\u2002 <b>Classification</b> \u2192 Output is a <b>CATEGORY</b> &nbsp;&nbsp;(spam / not-spam,  approved / rejected)', 'bodyL'),
], bg=SOFTBLUE))
story.append(SP(0.25))

story.append(P('\U0001F4CA  Comparison Table', 'h1'))
story.append(comparison_table(
    ['Aspect', 'Regression', 'Classification'],
    [
        ['Output Type',      'Continuous real number',          'Discrete class label'],
        ['Example Output',   '\u20b968,40,000 property price',  'APPROVED / REJECTED'],
        ['Loss Function',    'MSE / RMSE / MAE',                'Cross-Entropy / Log Loss'],
        ['Evaluation',       'R\u00b2, RMSE, MAE',              'Accuracy, Precision, Recall, F1'],
        ['Decision Boundary','No fixed boundary \u2014 fits a regression curve or surface',
                             'Learns a separating hyperplane or curved boundary'],
        ['Common Algorithms','Linear Reg., Ridge, Lasso, XGBoost Regressor',
                             'Logistic Reg., SVM, Random Forest Classifier, Na\u00efve Bayes'],
    ],
    col_widths=[USABLE*0.22, USABLE*0.39, USABLE*0.39]
))
story.append(SP(0.25))

story.append(P('\U0001F1EE\U0001F1F3  Real-World Indian Examples', 'h1'))
story.append(colbox([
    P('\U0001F3E6  Example 1 \u2014 HDFC Bank: EMI Amount Prediction  (Regression)', 'defh'),
    SP(0.05),
    P("HDFC's home loan engine collects applicant features \u2014 monthly income, CIBIL credit score, "
      "loan tenure, LTV ratio, property valuation \u2014 and predicts the exact monthly EMI "
      "(a continuous number in \u20b9). Since EMI can be \u20b912,500 or \u20b987,430.50, "
      "this is unmistakably a <b>Regression</b> problem.", 'body'),
    P('\u2022\u2002 Features (X):  Monthly Income, CIBIL Score, Loan Amount, Tenure, Age', 'bullet'),
    P('\u2022\u2002 Target (y):  EMI in \u20b9 per month  (e.g., \u20b924,350.75 / month)', 'bullet'),
], bg=SOFTGREEN))
story.append(SP(0.15))

story.append(colbox([
    P('\U0001F33E  Example 2 \u2014 Maharashtra Agriculture: Crop Yield Prediction  (Regression)', 'defh'),
    SP(0.05),
    P('The Maharashtra Government and ICAR use satellite remote-sensing data, soil health cards, '
      'rainfall records, and fertiliser usage to predict wheat / soybean yield in <b>quintals/hectare</b> '
      'for Vidarbha and Marathwada farmers. This continuous output guides MSP procurement and mandi supply planning.',
      'body'),
    P('\u2022\u2002 Features (X):  Rainfall (mm), Soil NPK index, Temperature, Sowing Date, Crop Variety', 'bullet'),
    P('\u2022\u2002 Target (y):  Yield in quintals/hectare  (e.g., 18.6 q/ha)', 'bullet'),
], bg=SOFTGREEN))
story.append(SP(0.15))

story.append(colbox([
    P('\U0001F4A1  Counter-example (Classification):  SBI loan default detection \u2014 the output is binary: '
      'DEFAULT (1) or NO DEFAULT (0). Classification models (Logistic Regression, XGBoost Classifier) '
      'are used here, not regression.',
      'note'),
], bg=SOFTORANGE))

story.append(HR())

# ─────────────────────────────────────────────────────────────
#  Q2  SLR vs MLR vs Regularised
# ─────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(KeepTogether([
    section_tag(2, 'Simple Linear Regression vs Multiple Linear Regression vs Regularised Regression'),
    SP(0.25),
]))

# SLR
story.append(P('\U0001F4D0  Simple Linear Regression (SLR)', 'h1'))
story.append(P(
    'Models the linear relationship between <b>one independent variable (feature)</b> and one dependent '
    'variable (target). It finds the best-fit straight line through the scatter of data points by '
    'minimising the Residual Sum of Squares.',
    'body'))
story.append(formula_box(
    'y = \u03b2\u2080  +  \u03b2\u2081 \u00d7 X  +  \u03b5',
    '\u03b2\u2080 = intercept (y-axis crossing),   \u03b2\u2081 = slope (rate of change),   \u03b5 = irreducible error term'
))
story.append(colbox([
    P('\u2022\u2002 <b>Example:</b>  Predicting exam marks (y) purely from hours studied (X).', 'bullet'),
    P('\u2022\u2002 <b>Limitation:</b>  Real-world outcomes almost never depend on just a single variable.', 'bullet'),
], bg=SOFTGREEN))
story.append(SP(0.25))

# MLR
story.append(P('\U0001F4D0  Multiple Linear Regression (MLR)', 'h1'))
story.append(P(
    'Extends SLR to <b>two or more independent variables</b>. The model fits a hyperplane '
    '(multi-dimensional flat surface) through the data. Each coefficient \u03b2\u1d62 represents '
    'the marginal effect of feature X\u1d62 on y, holding all other features constant.',
    'body'))
story.append(formula_box(
    'y = \u03b2\u2080  +  \u03b2\u2081X\u2081  +  \u03b2\u2082X\u2082  +  \u22ef  +  \u03b2\u209aX\u209a  +  \u03b5',
    'House Price = \u03b2\u2080 + \u03b2\u2081\u00d7GrLivArea + \u03b2\u2082\u00d7OverallQual + \u03b2\u2083\u00d7YearBuilt + \u2026'
))
story.append(colbox([
    P('\u2022\u2002 <b>Example:</b>  HDFC property valuation with 79 features \u2014 the Ames Housing problem.', 'bullet'),
    P('\u2022\u2002 <b>Problem:</b>  When p \u226b n or features are strongly correlated (multicollinearity), '
      'OLS coefficients become <b>unstable and blow up</b> \u2014 the model overfits noise.',
      'bullet'),
], bg=SOFTGREEN))
story.append(SP(0.25))

# Regularised
story.append(P('\U0001F4D0  Regularised Regression \u2014 Ridge (L2) &amp; Lasso (L1)', 'h1'))
story.append(P(
    'Regularisation adds a <b>penalty term</b> to the OLS loss that shrinks large coefficients '
    'toward zero, reducing model complexity and variance (overfitting) at the cost of a small '
    'increase in bias. This is the classical <b>Bias\u2013Variance Trade-off</b>.',
    'body'))
story.append(formula_box(
    'Ridge Loss  =  \u03a3(y\u1d62 \u2212 \u0177\u1d62)\u00b2  +  \u03bb \u00d7 \u03a3\u03b2\u1d62\u00b2          (L2 norm penalty)',
    'Lasso Loss  =  \u03a3(y\u1d62 \u2212 \u0177\u1d62)\u00b2  +  \u03bb \u00d7 \u03a3|\u03b2\u1d62|          (L1 norm penalty)'
))
story.append(SP(0.2))

story.append(comparison_table(
    ['Property', 'Ridge Regression (L2)', 'Lasso Regression (L1)'],
    [
        ['Penalty',                'Squared coefficients (\u2016\u03b2\u2016\u00b2)',   'Absolute values of coefficients (\u2016\u03b2\u2016\u2081)'],
        ['Coefficient Behaviour',  'All shrink toward zero; none become exactly 0', 'Forces some to exactly 0 \u2014 automatic feature selection'],
        ['Sparsity',               'Dense \u2014 all features retained',             'Sparse \u2014 irrelevant features eliminated'],
        ['Best For',               'Multicollinearity; many small correlated effects', 'High-dimensional data; automated feature pruning'],
        ['Hyperparameter Tuning',  'RidgeCV auto-selects optimal \u03bb',            'LassoCV auto-selects optimal \u03bb'],
        ['Project Result (Ames)',  'RMSE \u2248 $20,497 (\u03bb = 10)',               'RMSE \u2248 $20,058 (\u03bb = 0.001, 123 features \u2192 0)'],
    ],
    col_widths=[USABLE*0.22, USABLE*0.39, USABLE*0.39]
))
story.append(SP(0.15))
story.append(colbox([
    P('\U0001F4A1  Key Insight:  When \u03bb = 0, regularised regression reduces to plain OLS. '
      'As \u03bb \u2192 \u221e, all coefficients shrink to 0 (extreme underfitting). '
      'The optimal \u03bb is found by Cross-Validation.', 'note'),
], bg=SOFTORANGE))

story.append(HR())

# ─────────────────────────────────────────────────────────────
#  Q3  Overfitting & Underfitting
# ─────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(KeepTogether([
    section_tag(3, 'Explain Overfitting and Underfitting. How does Regularisation (L1/L2) help?'),
    SP(0.25),
]))

story.append(P('\U0001F4C9  Underfitting \u2014 High Bias', 'h1'))
story.append(P(
    'The model is <b>too simple</b> to capture the true relationship in the data. '
    'It performs poorly on <b>both training and test sets</b>. '
    'Like a student who barely studied \u2014 fails both mock exams and the final.',
    'body'))
story.append(SP(0.1))

story.append(P('\U0001F4C8  Overfitting \u2014 High Variance', 'h1'))
story.append(P(
    'The model <b>memorises training data noise</b> instead of learning the underlying pattern. '
    'It performs excellently on training data but <b>fails on unseen test data</b>. '
    'Like a student who only memorised previous-year papers \u2014 helpless when a new question pattern appears.',
    'body'))
story.append(SP(0.2))

story.append(comparison_table(
    ['Characteristic', 'Underfitting (High Bias)', 'Overfitting (High Variance)'],
    [
        ['Training Error',   'HIGH (cannot fit even training data)',   'Very LOW (memorises training data)'],
        ['Test Error',       'HIGH',                                   'HIGH (fails to generalise)'],
        ['Root Cause',       'Model too simple / too few features',    'Model too complex / too many features / noisy data'],
        ['Visual Sign',      'Flat line through curved data',          'Wiggly curve passing through every point'],
        ['Analogy',          'Under-prepared student',                 'Rote-memoriser student'],
        ['Fix',              'More features, polynomial terms, complex model', 'Regularisation, more training data, cross-validation'],
    ],
    col_widths=[USABLE*0.22, USABLE*0.39, USABLE*0.39]
))
story.append(SP(0.25))

story.append(P('\u2696\uFE0F  The Bias\u2013Variance Trade-Off', 'h1'))
story.append(formula_box(
    'Total Prediction Error  =  Bias\u00b2  +  Variance  +  Irreducible Noise',
    'Goal: simultaneously minimise Bias\u00b2 (underfitting) AND Variance (overfitting)'
))
story.append(SP(0.25))

story.append(P('\U0001F6E1\uFE0F  How Regularisation (L1/L2) Prevents Overfitting', 'h1'))
story.append(colbox([
    P('<b>Mechanism:</b>  Regularisation modifies the loss function by adding a penalty on '
      'coefficient magnitudes, forcing the optimiser to keep weights small and the model simple.', 'body'),
    SP(0.08),
    P('<b>Ridge (L2)  \u2014  Coefficient Shrinkage:</b>', 'h3'),
    P('\u2022\u2002 Penalises the <b>squared</b> values of coefficients.', 'bullet'),
    P('\u2022\u2002 Spreads weight evenly across correlated features \u2014 no coefficient is zeroed.', 'bullet'),
    P('\u2022\u2002 Geometrically: the L2 constraint region is a smooth sphere; optimal solution is a smooth interior point.', 'bullet'),
    SP(0.06),
    P('<b>Lasso (L1)  \u2014  Sparse Feature Selection:</b>', 'h3'),
    P('\u2022\u2002 Penalises the <b>absolute</b> values of coefficients.', 'bullet'),
    P('\u2022\u2002 The L1 constraint region is a diamond with sharp corners on the axes.', 'bullet'),
    P('\u2022\u2002 The optimal solution often lands <b>exactly on a corner</b>, forcing some \u03b2 = 0.', 'bullet'),
    P('\u2022\u2002 Result: automatic feature selection \u2014 only the most predictive features survive.', 'bullet'),
    SP(0.08),
    P('<b>Effect of \u03bb (Regularisation Strength):</b>', 'h3'),
    P('\u2022\u2002 \u03bb = 0 &nbsp;\u2192&nbsp; Plain OLS regression (may overfit if data is noisy)', 'bullet'),
    P('\u2022\u2002 \u03bb = small &nbsp;\u2192&nbsp; Mild regularisation (sweet spot)', 'bullet'),
    P('\u2022\u2002 \u03bb = large &nbsp;\u2192&nbsp; All coefficients \u2192 0 (underfitting)', 'bullet'),
    P('\u2022\u2002 Optimal \u03bb found via k-Fold Cross-Validation (RidgeCV / LassoCV)', 'bullet'),
], bg=SOFTBLUE))
story.append(SP(0.15))

story.append(colbox([
    P('\U0001F3E0  Project Evidence (Ames Housing):  Plain OLS achieved Test RMSE = $22,630. '
      'Ridge regularisation improved this to $20,497. Lasso further improved to $20,058 by '
      'pruning 123 redundant/collinear features, confirming that regularisation meaningfully '
      'reduces overfitting and coefficient instability.', 'note'),
], bg=SOFTORANGE))

story.append(HR())

# ─────────────────────────────────────────────────────────────
#  Q4  RMSE, MAE, R²
# ─────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(KeepTogether([
    section_tag(4, 'Define RMSE, MAE, and R\u00b2. When would you prefer RMSE over MAE?'),
    SP(0.25),
]))

# MAE
story.append(P('\U0001F4CF  Mean Absolute Error (MAE)', 'h1'))
story.append(formula_box(
    'MAE  =  \u00b9\u2215\u2099  \u00d7  \u03a3 |y\u1d62 \u2212 \u0177\u1d62|',
    'Average of absolute differences between actual and predicted values'
))
story.append(colbox([
    P('\u2022\u2002 Measures the <b>average absolute deviation</b> in the same units as the target (e.g., \u20b9).', 'bullet'),
    P('\u2022\u2002 <b>Robust to outliers</b> \u2014 each error contributes equally regardless of magnitude.', 'bullet'),
    P('\u2022\u2002 Interpretable: "On average, predictions are off by \u20b914,162."', 'bullet'),
    P('\u2022\u2002 Corresponds to <b>median-optimal prediction</b> (minimising MAE gives median prediction).', 'bullet'),
], bg=SOFTBLUE))
story.append(SP(0.2))

# RMSE
story.append(P('\U0001F4CF  Root Mean Squared Error (RMSE)', 'h1'))
story.append(formula_box(
    'RMSE  =  \u221a[ \u00b9\u2215\u2099  \u00d7  \u03a3(y\u1d62 \u2212 \u0177\u1d62)\u00b2 ]',
    'Square root of the average squared differences \u2014 same units as target'
))
story.append(colbox([
    P('\u2022\u2002 <b>Squares errors</b> before averaging \u2014 larger errors are penalised <b>much more heavily</b>.', 'bullet'),
    P('\u2022\u2002 Sensitive to outliers; a few large errors can dominate the RMSE value.', 'bullet'),
    P('\u2022\u2002 Corresponds to <b>mean-optimal prediction</b> (minimising RMSE gives mean prediction).', 'bullet'),
    P('\u2022\u2002 <b>Always: RMSE \u2265 MAE</b>.  When RMSE \u226b MAE, large outlier errors are present.', 'bullet'),
], bg=SOFTBLUE))
story.append(SP(0.2))

# R²
story.append(P('\U0001F4CF  R\u00b2 \u2014 Coefficient of Determination', 'h1'))
story.append(formula_box(
    'R\u00b2  =  1  \u2212  [ \u03a3(y\u1d62 \u2212 \u0177\u1d62)\u00b2  \u00f7  \u03a3(y\u1d62 \u2212 \u0233)\u00b2 ]',
    '\u0233 = mean of actual values    |    R\u00b2 = 0.93 means model explains 93% of variance in y'
))
story.append(colbox([
    P('\u2022\u2002 <b>Scale-free</b> measure, ranges from \u2212\u221e to 1.0 (higher is better).', 'bullet'),
    P('\u2022\u2002 R\u00b2 = 1.0 \u2192 perfect predictions. &nbsp; R\u00b2 = 0 \u2192 no better than predicting the mean. &nbsp; R\u00b2 < 0 \u2192 worse than mean.', 'bullet'),
    P('\u2022\u2002 Does <b>not</b> penalise model complexity \u2014 use <b>Adjusted R\u00b2</b> when comparing models with different feature counts.', 'bullet'),
], bg=SOFTBLUE))
story.append(SP(0.25))

# RMSE vs MAE table
story.append(P('\u2696\uFE0F  When to Prefer RMSE over MAE?', 'h1'))
story.append(comparison_table(
    ['Scenario', 'Preferred Metric', 'Reasoning'],
    [
        ['Large outliers are rare but <b>extremely costly</b>\n(e.g., property price error of \u20b950L)',
         'RMSE',
         'Quadratic penalty forces model to minimise catastrophic mispricings'],
        ['Data is <b>noisy</b> with many natural outliers\n(e.g., IoT sensor readings)',
         'MAE',
         'Equal treatment of all errors; outliers do not dominate the metric'],
        ['Business cost of error grows <b>non-linearly</b>\n(e.g., HDFC loan default risk)',
         'RMSE',
         'Squared penalty aligns with asymmetric real-world cost functions'],
        ['You want a <b>median-optimal</b> prediction\n(e.g., income distribution with skew)',
         'MAE',
         'Minimising MAE yields the conditional median \u2014 more robust for skewed targets'],
        ['Comparing models or tuning hyperparameters',
         'Both',
         'RMSE for sensitivity to large errors; MAE for robust overall performance view'],
    ],
    col_widths=[USABLE*0.36, USABLE*0.18, USABLE*0.46]
))
story.append(SP(0.15))
story.append(colbox([
    P('\U0001F3E0  PropTech Context (NoBroker / HDFC):  RMSE is preferred for property price prediction '
      'because a \u20b950 lakh over-valuation is <b>catastrophically worse</b> than a \u20b95 lakh error '
      'for a homebuyer taking a 20-year mortgage. RMSE\'s squared penalty forces the model to avoid '
      'such extreme misvaluations. Our Ames Housing project: RMSE = $19,636 vs MAE = $14,162 \u2014 '
      'the gap indicates a few expensive homes are harder to predict precisely.', 'note'),
], bg=SOFTORANGE))

story.append(HR())

# ─────────────────────────────────────────────────────────────
#  Q5  Cross-Validation
# ─────────────────────────────────────────────────────────────
story.append(PageBreak())
story.append(KeepTogether([
    section_tag(5, 'What is Cross-Validation (k-Fold)? Why preferred over a single train-test split?'),
    SP(0.25),
]))

story.append(P('\U0001F4D6  What is Cross-Validation?', 'h1'))
story.append(P(
    'Cross-Validation (CV) is a <b>statistical resampling technique</b> that evaluates how well '
    'a machine learning model generalises to <b>independent, unseen data</b>. Instead of relying '
    'on a single arbitrary train-test split, CV systematically rotates the holdout set to produce '
    'a robust, low-variance estimate of true model performance.',
    'body'))
story.append(SP(0.2))

story.append(P('\U0001F504  k-Fold Cross-Validation \u2014 Step-by-Step', 'h1'))
story.append(step_box([
    'Shuffle the full dataset randomly.',
    'Divide dataset into <b>k equal-sized folds</b> (subsets). Standard choice: k = 5 or 10.',
    'For each fold i (from 1 to k):  use fold i as <b>Validation set</b>; train on remaining k\u22121 folds; record validation score (e.g., RMSE).',
    'Final CV Score = <b>Mean \u00b1 Std Deviation</b> of all k validation scores.',
]))
story.append(SP(0.2))

# Fold diagram box
story.append(colbox([
    P('\U0001F5FA\uFE0F  Visual Fold Diagram (k = 5):', 'h2'),
    SP(0.05),
    P('Fold 1:   [ \u25A0 TEST \u25A0 ] [ train ] [ train ] [ train ] [ train ]', 'code'),
    P('Fold 2:   [ train ] [ \u25A0 TEST \u25A0 ] [ train ] [ train ] [ train ]', 'code'),
    P('Fold 3:   [ train ] [ train ] [ \u25A0 TEST \u25A0 ] [ train ] [ train ]', 'code'),
    P('Fold 4:   [ train ] [ train ] [ train ] [ \u25A0 TEST \u25A0 ] [ train ]', 'code'),
    P('Fold 5:   [ train ] [ train ] [ train ] [ train ] [ \u25A0 TEST \u25A0 ]', 'code'),
    SP(0.08),
    P('CV RMSE  =  Mean ( RMSE\u2081, RMSE\u2082, RMSE\u2083, RMSE\u2084, RMSE\u2085 )  \u00b1  Std Dev', 'formula'),
], bg=SOFTTEAL))
story.append(SP(0.25))

story.append(P('\u2705  Why Preferred Over a Single Train-Test Split?', 'h1'))
story.append(comparison_table(
    ['Issue', 'Single Train-Test Split', 'k-Fold Cross-Validation'],
    [
        ['Data Efficiency',
         '~20% of data wasted for testing; never used for training.',
         'Every data point used for BOTH training AND validation across different folds. Maximum utilisation.'],
        ['Score Variance / Reliability',
         'Score heavily depends on which rows ended up in test set (luck of the draw). High variance.',
         'Averages over k independent evaluations. Statistically robust, low-variance performance estimate.'],
        ['Overfitting Detection',
         'One lucky split can give falsely optimistic results.',
         'Harder to overfit across k different validation sets. Better true generalisation estimate.'],
        ['Hyperparameter Tuning',
         'Tuning to a single test set causes data leakage (you effectively train on the test set).',
         'CV provides uncontaminated evaluation for hyperparameter selection (RandomizedSearchCV).'],
        ['Small Datasets',
         'Losing 20% to testing is very costly when data is scarce.',
         'k-Fold makes full use of limited data \u2014 critical for medical/agricultural datasets.'],
        ['Reproducibility',
         'Results change with random seed / split choice.',
         'With shuffle=True and fixed random_state, results are stable and reproducible.'],
    ],
    col_widths=[USABLE*0.20, USABLE*0.37, USABLE*0.43]
))
story.append(SP(0.2))

story.append(colbox([
    P('<b>Choosing k:</b>', 'h3'),
    P('\u2022\u2002 <b>k = 5 or 10</b> \u2192 Standard choice; good balance of computation vs. estimate reliability.', 'bullet'),
    P('\u2022\u2002 <b>k = n (LOOCV \u2014 Leave-One-Out CV)</b> \u2192 Maximum data use; computationally expensive; high variance in the estimate.', 'bullet'),
    P('\u2022\u2002 <b>Stratified k-Fold</b> \u2192 For classification; maintains class label proportion in each fold.', 'bullet'),
    P('\u2022\u2002 <b>Repeated k-Fold</b> \u2192 Runs k-Fold multiple times with different shuffles; even more stable estimate.', 'bullet'),
], bg=SOFTBLUE))
story.append(SP(0.15))

story.append(colbox([
    P('\U0001F3E0  Our Project (Ames Housing):  5-Fold CV on Tuned XGBoost gave Log RMSE = 0.1197 \u00b1 small \u03c3. '
      'This closely aligned with the holdout test RMSE ($19,636), confirming no overfitting and '
      'that the model generalises well beyond the 80% training set.', 'note'),
], bg=SOFTORANGE))

story.append(HR())

# ─────────────────────────────────────────────────────────────
#  FINAL SUMMARY TABLE
# ─────────────────────────────────────────────────────────────
story.append(PageBreak())

story.append(P('\U0001F4CB  Quick Reference Summary \u2014 All 5 Questions', 'h1'))
story.append(SP(0.1))

story.append(comparison_table(
    ['#', 'Topic', 'Core Idea', 'Key Formula / Rule of Thumb'],
    [
        ['Q1',
         'Regression vs Classification',
         'Regression \u2192 continuous number output. Classification \u2192 discrete category label.',
         'Output is a number \u2192 Regression. Output is a class \u2192 Classification.'],
        ['Q2',
         'SLR vs MLR vs Regularised',
         'SLR: one feature. MLR: many features. Regularised: adds penalty \u03bb to control coefficient magnitude.',
         'Ridge: L2 penalty (all \u03b2 shrink). Lasso: L1 penalty (some \u03b2 \u2192 0). Optimal \u03bb via CV.'],
        ['Q3',
         'Overfitting vs Underfitting',
         'Underfitting: model too simple, high bias. Overfitting: model memorises noise, high variance.',
         'Total Error = Bias\u00b2 + Variance + Noise. Balance via regularisation + CV.'],
        ['Q4',
         'RMSE, MAE & R\u00b2',
         'RMSE penalises large errors quadratically. MAE treats all errors equally. R\u00b2 measures explained variance.',
         'RMSE \u2265 MAE always. R\u00b2 = 1 \u2192 perfect. Prefer RMSE when large errors are very costly.'],
        ['Q5',
         'Cross-Validation',
         'Rotate holdout fold k times. Average k scores for a robust, low-variance evaluation.',
         'k = 5 or 10 (standard). CV Score = Mean \u00b1 Std of k validation fold scores.'],
    ],
    col_widths=[USABLE*0.05, USABLE*0.17, USABLE*0.42, USABLE*0.36]
))
story.append(SP(0.4))
story.append(HR(NAVY, 1.5))
story.append(SP(0.15))
story.append(P(
    'ML Theory Notes  \u2022  Supervised Learning \u2014 Regression Deep Dive  \u2022  Final Examination Preparation',
    'footer'))
story.append(P(
    'Ames Housing Project  \u2022  PropTech Valuation (NoBroker / MagicBricks)  \u2022  XGBoost Champion: R\u00b2 = 0.930, RMSE = $19,636',
    'footer'))

# ─────────────────────────────────────────────────────────────
#  BUILD THE PDF
# ─────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    'ML_Theory_Notes.pdf',
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=1.8*cm,  bottomMargin=1.8*cm,
    title='ML Core Theory Notes',
    author='Supervised Learning Exam Prep',
)
doc.build(story)
print(f"PDF built successfully: ML_Theory_Notes.pdf")

