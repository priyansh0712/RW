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
# 🧩 Data Modeling

<img width="1517" height="720" alt="image" src="https://github.com/user-attachments/assets/40fc6c26-81fc-4586-80e7-a392472abdf9" />


A clean and optimized Star Schema model was created to improve dashboard performance, filtering efficiency, and relationship management.

---

## 📁 Tables Used

| Table | Type | Description |
|-------|------|-------------|
| Orders | Fact Table | Main transactional sales dataset |
| Customers | Dimension Table | Customer-related information |
| Products | Dimension Table | Product and category details |
| DateTable | Dimension Table | Calendar table for time intelligence |

---

## 🔗 Relationships

| From Table | To Table | Relationship |
|------------|----------|--------------|
| Orders | Customers | Many → One |
| Orders | Products | Many → One |
| Orders | DateTable | Many → One |

---

## 📌 Modeling Features

- Star Schema Data Model
- Single Direction Cross Filtering
- Optimized Relationships
- Hidden Unnecessary Columns
- DateTable Marked as Official Date Table
- Improved Filtering Performance
- Structured Data Hierarchy

---

## ⚙️ Additional Steps Performed

- Data cleaning using Power Query
- Removed null and duplicate values
- Corrected data types
- Created calculated columns and measures
- Optimized model for drillthrough and slicer interactions

# 🧩 Dashboard Pages

---

# 🔹 Page 1 — Overview

<img width="1182" height="678" alt="image" src="https://github.com/user-attachments/assets/8d7ef6e7-98d1-4f4a-9f17-cf3b38edf951" />

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

<img width="1186" height="678" alt="image" src="https://github.com/user-attachments/assets/aabeff60-8b97-4cd6-b607-4291e575258c" />

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

<img width="1182" height="680" alt="image" src="https://github.com/user-attachments/assets/678be86e-0a3a-4435-914e-6283f34f9221" />

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

<img width="1182" height="677" alt="image" src="https://github.com/user-attachments/assets/a527a661-149b-4bec-aacf-f87ac0be165e" />
<img width="707" height="522" alt="image" src="https://github.com/user-attachments/assets/3718599e-c678-4f9b-978e-aca0398ba929" />


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

<img width="963" height="462" alt="image" src="https://github.com/user-attachments/assets/fc530b3e-2238-4b72-88bc-af1c9747db79" />

A custom tooltip page designed using a Gauge Visual.

### 📌 Tooltip Features
- Dynamic hover interaction
- Gauge-based KPI visualization
- Context-sensitive metric display
---

# 📱 Mobile Layout

A fully optimized mobile-friendly layout was created for better accessibility and responsive dashboard viewing on smartphones.

### 📌 Mobile Features
- Responsive KPI arrangement
- Optimized visual scaling
- Vertical scrolling layout
- Touch-friendly slicers and buttons
- Simplified navigation experience

### 📊 Mobile Pages Included
- Overview
- Customer Insights
- Product Analysis
- Deep Dive

The mobile layout ensures a smooth and user-friendly dashboard experience across different screen sizes.

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
<img width="245" height="401" alt="image" src="https://github.com/user-attachments/assets/cb9ff258-b54a-4366-bf49-e0a0378601cf" /><img width="232" height="523" alt="image" src="https://github.com/user-attachments/assets/5317748c-3975-4916-8f7b-b6bf6b23ac09" />



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
