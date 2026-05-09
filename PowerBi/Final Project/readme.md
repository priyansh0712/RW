# 📊 Financial Performance Dashboard — Power BI End-to-End Project

A complete Power BI dashboard project focused on Financial Performance Analysis using advanced DAX, interactive visuals, drillthrough pages, custom tooltips, and modern dashboard design principles.

---

# 🚀 Project Overview

An interactive multi-page Power BI reporting solution designed with a modern dark-themed financial dashboard UI.

The dashboard provides detailed insights into:
- Sales Performance
- Customer Insights
- Product Analysis
- Customer-Level Drillthrough Analytics

The report includes:
- Dynamic KPI Cards
- Drillthrough Analysis
- Interactive Filtering
- Custom Tooltip Design
- Bookmark-Based Reset Functionality
- Modern Navigation Layout

---

# 🗂️ Project Files

| File Name | Description |
|-----------|-------------|
| 📄 `Financial_Performance.pbix` | Main Power BI dashboard file |
| 📘 `README.md` | Project documentation |
| 📁 `Dataset Files` | Raw dataset used in the project |
| 🖼️ `Dashboard Preview` | Dashboard screenshots |

---

# 📁 Data Tables Used

| Table | Description |
|-------|-------------|
| Orders | Main sales transaction dataset |
| Customers | Customer-related information |
| Products | Product and category details |
| DateTable | Calendar table for time intelligence |

---

# 🧩 Dashboard Pages

---

# 🔹 Page 1 — Overview

Main financial dashboard displaying company-wide sales performance and category insights.

### 📌 KPI Cards
- 💰 Total Sales
- 💸 Total Cost
- 📈 Total Profit
- 📦 Total Orders

### 📊 Visuals Used
- Sankey Chart — Sales Development Flow
- Horizontal Bar Chart — Sales by Region
- Column Chart — Monthly Sales Trend
- Donut Chart — Sales by Category

### 🎛️ Features
- Interactive slicers
- Dynamic KPI growth indicators
- Modern sidebar navigation
- Bookmark-based slicer reset button
- Custom tooltip interaction

---

# 🔹 Page 2 — Customer Insights

Customer-focused dashboard for analyzing customer performance and segment contribution.

### 📌 KPI Cards
- 👥 Total Customers
- 🔁 Repeat %
- 💵 Revenue per Customer
- 📈 Customer Growth %

### 📊 Visuals Used
- 100% Stacked Column Chart — Segment Analysis
- Customer Matrix Table — Customer Sales Breakdown

### 📋 Matrix Includes
- Full Name
- Segment
- Units Sold
- Total Revenue

### 🎛️ Features
- Segment-level analysis
- Interactive filtering
- Customer performance comparison

---

# 🔹 Page 3 — Product Analysis

Product-focused analysis dashboard showing top-performing products and category-level contribution.

### 📌 KPI Cards
- 📦 Total Products
- 💰 Revenue
- 🏆 Top Category
- 📈 Product Growth %

### 📊 Visuals Used
- Horizontal Bar Chart — Top 10 Products
- Waterfall Chart — Sales by Category

### 📌 Insights Provided
- Best-selling products
- Category contribution analysis
- Product revenue comparison

---

# 🔹 Page 4 — Deep Dive (Drillthrough Page)

Customer-level drillthrough analysis page designed for detailed customer insights.

> **How to Access:**  
Right-click on any customer visual → Drillthrough → Deep Dive

### 📌 KPI Cards
- 💰 Sales
- 📦 Avg Order Value
- 📈 Profit
- 🛒 Orders

### 📊 Visuals Used
- Area Chart — Purchase Trend
- Funnel Chart — Category Performance

### 📋 Purpose
Provides detailed analysis of selected customers including:
- Purchase trends
- Category-wise spending
- Revenue contribution
- Order behavior

---

# 🔹 Tooltip Page

A custom tooltip page designed using a Gauge Visual.

### 📌 Tooltip Features
- Dynamic hover interaction
- Gauge-based KPI visualization
- Context-sensitive metric display

---

# 🎨 Dashboard Design Features

- Modern Dark Purple UI Theme
- Premium KPI Card Design
- Rounded Visual Containers
- Interactive Sidebar Navigation
- Dynamic Growth Indicators
- Responsive Layout Structure
- Custom Styled Slicers
- Smooth Visual Alignment

---

# 📌 Key Insights

- ✅ Office Supplies is one of the highest-performing product categories
- ✅ Consumer segment contributes a major share of total revenue
- ✅ West and South regions generate strong sales performance
- ✅ Customer growth remains positive across multiple segments
- ✅ Product category contribution varies significantly
- ✅ Drillthrough analysis helps identify high-value customers quickly

---

# 🛠️ Tools & Features Used

| Tool / Feature | Usage |
|----------------|-------|
| Power BI Desktop | Dashboard Development |
| Power Query | Data Cleaning & Transformation |
| DAX | KPI & Measure Calculations |
| Drillthrough | Customer-Level Analysis |
| Bookmarks | Reset Slicer Functionality |
| Custom Tooltip | Gauge-Based Tooltip Page |
| Conditional Formatting | KPI & Matrix Styling |
| Slicers | Interactive Filtering |
| Sankey Visual | Sales Flow Analysis |
| Waterfall Chart | Category Comparison |
| Star Schema | Data Modeling |

---

# 📐 DAX Measures Used

## Total Sales
```DAX
Total Sales =
SUM(Orders[Total Revenue])
```

---

## Total Profit
```DAX
Total Profit =
SUM(Orders[Profit])
```

---

## Revenue per Customer
```DAX
Revenue per Customer =
DIVIDE(
    [Total Sales],
    [Total Customers]
)
```

---

## Product Growth %
```DAX
Product Growth % =
DIVIDE(
    [Current Sales]-[Last Year Sales],
    [Last Year Sales]
)
```

---

## Repeat Customer %
```DAX
Repeat Customer % =
DIVIDE(
    [Repeat Customers],
    [Total Customers]
)
```

---

## Additional Measures
- KPI Growth Indicators
- Dynamic Tooltip Measures
- Category Contribution Measures
- Time Intelligence Measures
- Customer Performance Metrics
- Product Analysis Calculations
- Interactive Filter Measures
- Drillthrough Context Measures
- etc.

---

# 📱 Dashboard Navigation

The report includes:
- Sidebar Menu Navigation
- Drillthrough Navigation
- Dynamic Filtering
- Reset All Slicers Button
- Interactive Page Switching

---

# 👨‍💻 Priyansh Vekariya

📍 Ahmedabad, Gujarat

⭐ Interactive UI · Advanced DAX · Premium Dashboard Design