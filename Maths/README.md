# 📊 Regional Sales Bottleneck Analysis Dashboard

## 📌 Project Title
**Unlocking Revenue: Identifying Bottlenecks in Regional Sales Pipeline**

---

# 📖 Project Overview

This project analyzes regional sales transaction data using **SQL** and **Power BI** to identify business bottlenecks such as:

- High cancellation and return rates
- Revenue loss patterns
- Underperforming regions
- Product performance
- Sales agent performance

The main objective of this project is to transform raw sales data into meaningful business insights through data analysis and visualization.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| MySQL | Data Storage & SQL Analysis |
| Power BI | Dashboard Visualization |
| CSV / Excel | Dataset Preparation |

---

# 📂 Dataset Information

Dataset Name:

```text
RegionalSales2025.csv
```

## Dataset Columns

| Column Name | Description |
|---|---|
| OrderID | Unique order identifier |
| Date | Transaction date |
| CustomerID | Unique customer identifier |
| Region | Sales region |
| ProductName | Product name |
| Category | Product category |
| Quantity | Number of units sold |
| UnitPrice | Price per unit |
| TotalAmount | Total transaction amount |
| OrderStatus | Completed / Cancelled / Returned |
| SalesAgent | Sales representative |

---

# 🛢️ SQL Analysis Performed

The following SQL analyses were performed:

1. Monthly Sales Trend Analysis
2. Cancellation & Return Percentage by Region
3. Top Products Causing Revenue Loss
4. Average Order Value by Category
5. Top Performing Sales Agents
6. Category-wise Sales Contribution
7. Frequent Return Customers

---

# 📊 Power BI Dashboard Features
<img width="1298" height="727" alt="image" src="https://github.com/user-attachments/assets/66b35f8d-b1b6-44bb-b8d0-dfa3346ae059" />


The dashboard includes:

- Matrix / Heatmap (Region vs Category Sales)
- Stacked Bar Chart (Order Status Analysis)
- Monthly Sales Trend Line Chart
- KPI Cards:
  - Total Completed Sales
  - Total Cancellations
  - Average Order Value
  - Most Returned Product

---

# 🎛️ Interactive Filters

The dashboard contains slicers for:

- Region
- Category
- SalesAgent

These filters improve dashboard interactivity and allow dynamic analysis.

---

# 📈 Key Business Insights

- Some regions showed significantly higher cancellation rates.
- Electronics products generated maximum returns.
- Certain sales agents outperformed others in completed revenue.
- Some categories contributed lower overall sales.

These insights can help businesses improve operational efficiency and decision-making.

---

# 🔄 Project Workflow

```text
Dataset Creation
        ↓
CSV Import into MySQL
        ↓
SQL Data Analysis
        ↓
Export Results
        ↓
Power BI Dashboard Creation
        ↓
Business Insights & Visualization
```

---

# 📁 Project Files

| File Name | Description |
|---|---|
| RegionalSales2025.csv | Sales dataset |
| SalesBottleneck.sql | SQL queries |
| BottleneckDashboard.pbix | Power BI dashboard |
| ExecutiveSummary.txt | Final insights summary |

---

# ✅ Conclusion

This project demonstrates how SQL and Power BI can be used together to analyze sales data, identify operational bottlenecks, and generate actionable business insights using interactive dashboards and KPI tracking.

---

# 👨‍💻 Developed By

**Priyansh Vekariya**
