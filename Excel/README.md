# 📊 PR2 Sales Analytics — Excel Workbook

A comprehensive Excel workbook covering 10 data analytics tasks using a real-world sales dataset (200 records, Apr 2024 – Apr 2025).

---

## 📁 Dataset Overview

| Field | Description |
|---|---|
| `Customer_ID` | Unique customer identifier (CUST001–CUST030) |
| `Customer_Name` | Customer full name |
| `Region` | Sales region: North, South, East, West, Central |
| `Product_Category` | Books, Clothing, Electronics, Furniture, Office Supplies |
| `Sales` | Order revenue in USD |
| `Quantity` | Units sold per order |
| `Discount` | Discount rate applied (0%–20%) |
| `Order_Date` | Date of order (DD-MM-YYYY) |
| `Profit` | Net profit per order in USD |

**200 total records** spanning 13 months across 30 unique customers.

---

## 🗂️ Workbook Structure

| Sheet | Task | Topic |
|---|---|---|
| `INDEX` | — | Workbook navigation guide |
| `Raw Data` | 6 | Source data + Timestamp column |
| `Top10_Customers` | 1 | Conditional Formatting |
| `WhatIf_Analysis` | 2 | WHAT-IF Analysis |
| `Linear_Regression` | 3 | Regression (ToolPak Style) |
| `Descriptive_Stats` | 4 | Descriptive Statistics |
| `Monthly_Arrows` | 5 | Symbols & Custom Formatting |
| `HighValue_Customers` | 7 | INDEX-MATCH + Segmentation |
| `Pivot_Analysis` | 8 | Pivot Tables |
| `Charts` | 9 | Bar, Line & Pie Charts |
| `Dashboard` | 10 | KPI Dashboard |

---

## ✅ Task Details

### Task 1 — Conditional Formatting: Top 10 Customers
**Sheet:** `Top10_Customers`

- Customers ranked by total purchase (SUMIF aggregation across all orders).
- **Top 3** highlighted in Orange, **Ranks 4–7** in Green, **Ranks 8–10** in Blue.
- Color scale applied to the Total Sales column (red → yellow → green).
- Profit Margin % calculated for each customer.

---

### Task 2 — WHAT-IF Analysis: Discount Impact on Profit
**Sheet:** `WhatIf_Analysis`

- 8 discount scenarios tested: 0%, 5%, 10%, Base Average, 20%, 25%, 30%, 40%.
- Formula used:
  ```
  Projected Profit = Base Profit × [(1 − New Discount%) ÷ (1 − Avg Discount%)]
  ```
- Columns show: Projected Profit, Change in $ vs Base, Change in % vs Base.
- Arrow indicators:
  - `⬆ PROFIT GAIN` — discount lower than base
  - `⬇ PROFIT LOSS` — discount higher than base
  - `➡ NO CHANGE` — same as base

---

### Task 3 — Linear Regression (Profit vs Sales)
**Sheet:** `Linear_Regression`

ToolPak-style regression output includes:

| Section | Contents |
|---|---|
| Regression Statistics | Multiple R, R², Adjusted R², Standard Error, Observations |
| ANOVA Table | df, SS, MS, F-statistic for Regression & Residual |
| Coefficients | Intercept, Slope (b1), Std Error, t-Stat |
| Prediction Table | Predicted Profit for Sales = $500 to $2,000 with 95% CI |

**Regression Equation:**
```
Profit = b0 + b1 × Sales
```
Interpretation: For every $1 increase in Sales, Profit increases by $b1.

---

### Task 4 — Descriptive Statistics
**Sheet:** `Descriptive_Stats`

Full statistics computed for **Sales, Profit, Quantity, and Discount**:

- Count, Mean, Standard Deviation, Variance
- Minimum, Maximum, Range
- Median, Q1, Q3, IQR
- Skewness, Kurtosis
- Sum, Coefficient of Variation (CV%)

Key insights panel included below the stats tables.

---

### Task 5 — Up/Down Arrows on Monthly Sales Growth
**Sheet:** `Monthly_Arrows`

- Month-over-month (MoM) change calculated in $ and %.
- Custom arrow symbols applied based on growth rate:

| Arrow | Meaning | Threshold |
|---|---|---|
| `▲ Strong Growth` | Green | MoM > +5% |
| `↑ Moderate Growth` | Light Green | MoM 0% to +5% |
| `→ No Change` | Gray | MoM = 0% |
| `↓ Slight Decline` | Orange | MoM 0% to −5% |
| `▼ Sharp Decline` | Red | MoM < −5% |

---

### Task 6 — Timestamp Column
**Sheet:** `Raw Data` → Column J

- Every data row includes a timestamp using:
  ```excel
  =NOW()
  ```
- Formatted as `DD-MM-YYYY HH:MM`.
- Auto-updates each time the workbook is recalculated.

---

### Task 7 — High-Value Customers (INDEX-MATCH)
**Sheet:** `HighValue_Customers`

- All 30 customers aggregated by: Total Sales, Total Profit, Order Count, Avg Order Value, Top Category.
- Segmented into 4 tiers:

| Tier | Threshold |
|---|---|
| 🏆 Platinum | Top 10% by Sales |
| 🥇 Gold | 75th–90th percentile |
| 🥈 Silver | 25th–75th percentile |
| 🥉 Bronze | Bottom 25% |

- **Live INDEX-MATCH lookup** at the bottom of the sheet — edit the Customer ID cell to instantly retrieve Name, Sales, Profit, and Segment using:
  ```excel
  =IFERROR(INDEX(range, MATCH(lookup_value, lookup_range, 0)), "Not Found")
  ```

---

### Task 8 — Pivot Table
**Sheet:** `Pivot_Analysis`

Two pivot tables:
1. **Total Sales** by Region × Product Category (with Grand Totals)
2. **Total Profit** by Region × Product Category (with Grand Totals)

Rows = Regions (Central, East, North, South, West)
Columns = Product Categories (Books, Clothing, Electronics, Furniture, Office Supplies)

---

### Task 9 — Charts
**Sheet:** `Charts`

| Chart Type | X-Axis | Y-Axis | Insight |
|---|---|---|---|
| **Clustered Bar** | Region | Sales & Profit | Side-by-side regional comparison |
| **Line Chart** | Month | Monthly Sales | Trend over 13 months |
| **Pie Chart** | Product Category | % of Total Sales | Category share breakdown |

All charts include titles, axis labels, and data labels/percentages.

---

### Task 10 — Dashboard
**Sheet:** `Dashboard`

- **8 KPI tiles** (2 rows × 4 columns):
  - Total Sales, Total Profit, Total Orders, Avg Order Value
  - Top Customer, Top Category, Top Region, Avg Discount
- **3 embedded charts**: Regional bar, Category pie, Monthly line trend
- **8-point insights panel** summarizing key findings from the data

---

## 🔢 Key Metrics (Summary)

| Metric | Value |
|---|---|
| Total Records | 200 |
| Total Sales | ~$193,000+ |
| Total Profit | ~$69,000+ |
| Profit Margin | ~35–36% |
| Date Range | Apr 2024 – Apr 2025 |
| Unique Customers | 30 |
| Unique Regions | 5 |
| Product Categories | 5 |
| Formulas in Workbook | 204 (0 errors) |

---

## 🛠️ Tools & Techniques Used

- **Microsoft Excel** (compatible with Excel 2016+)
- `SUMIF`, `AVERAGEIF`, `COUNTIF` — aggregation formulas
- `INDEX` + `MATCH` — dynamic lookup
- `NOW()` — live timestamp
- `IFERROR` — error handling
- Conditional Formatting — color scales, formula-based rules
- Data Analysis ToolPak — regression & descriptive stats (replicated manually for portability)
- Pivot Tables — multi-dimensional aggregation
- Charts — Bar, Line, Pie with labels

---

## 📌 Notes

- The `=NOW()` timestamp column recalculates every time the file is opened or recalculated — this is expected behavior.
- The INDEX-MATCH lookup cell in `HighValue_Customers` is editable — change the Customer ID to query any of the 30 customers.
- All charts in the `Dashboard` sheet pull data from the `Charts` sheet — do not delete or rename that sheet.
- The workbook was verified with **zero formula errors** before delivery.
