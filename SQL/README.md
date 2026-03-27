# 📊 Order Management Database System

## 📌 Overview

This project demonstrates a basic **Order Management System** using SQL.
It includes tables for customers, products, orders, and order details, along with queries to perform real-world operations like revenue calculation and product analysis.

---

## 🗂️ Database Structure

### 1. Customers Table

Stores customer information.

* `customer_id` (Primary Key)
* `name`
* `email`
* `address`

---

### 2. Products Table

Stores product details.

* `ProductID` (Primary Key)
* `ProductName`
* `Price`
* `Stock`

---

### 3. Orders Table

Stores order-level data.

* `OrderID` (Primary Key)
* `CustomerID` (Foreign Key)
* `OrderDate`
* `TotalAmount`

---

### 4. OrderDetails Table

Stores product-level order details.

* `OrderDetailID` (Primary Key)
* `OrderID` (Foreign Key)
* `ProductID` (Foreign Key)
* `Quantity`
* `SubTotal`

---

## 🔗 Relationships

* One **Customer → Many Orders**
* One **Order → Many OrderDetails**
* One **Product → Many OrderDetails**

---

## ⚙️ Key Features

* Data insertion for all tables
* Foreign key constraints
* Aggregation queries (SUM, COUNT)
* Ranking queries (Top products)
* Filtering queries

---

## 🧪 Sample Queries

### 🔹 Get all order details for a specific order

```sql
SELECT * FROM order_details
WHERE OrderID = 1;
```

---

### 🔹 Calculate total revenue

```sql
SELECT SUM(SubTotal) AS total_revenue
FROM order_details;
```

---

### 🔹 Top 3 most ordered products

```sql
SELECT ProductID, SUM(Quantity) AS total_quantity
FROM order_details
GROUP BY ProductID
ORDER BY total_quantity DESC
LIMIT 3;
```

---

### 🔹 Count how many times a product is sold

```sql
SELECT ProductID, COUNT(*) AS times_sold
FROM order_details
WHERE ProductID = 2
GROUP BY ProductID;
```

---

## ⚠️ Limitations

* `SubTotal` is stored instead of calculated dynamically
* No indexing for performance optimization
* No normalization for advanced scalability

---

## 🚀 Future Improvements

* Add indexing for faster queries
* Normalize schema (separate calculations)
* Add triggers for automatic subtotal calculation
* Build API or UI layer on top of database

---

## 🧠 Learning Outcomes

* SQL table design
* Primary & Foreign Keys
* Joins and Relationships
* Aggregation functions (SUM, COUNT)
* Real-world query building