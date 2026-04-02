# 📊 SQL Practice – Joins, Subqueries, Functions & Aggregations

## 📌 Overview

This project demonstrates core SQL concepts using a structured dataset.
It includes examples of:

* Joins (INNER, LEFT, RIGHT, FULL workaround)
* Subqueries
* Aggregate functions
* Date & string functions
* Window functions
* Conditional logic (CASE)

The dataset is designed to support all queries meaningfully (not random data).

---

## 🗂️ Tables Used

### 1. Customers

Stores customer details.

* `CustomerID` (Primary Key)
* `FirstName`
* `LastName`
* `Email`
* `RegistrationDate`

---

### 2. Orders

Stores order information.

* `OrderID` (Primary Key)
* `CustomerID` (Foreign Key)
* `OrderDate`
* `TotalAmount`

---

### 3. Employees

Stores employee details.

* `EmployeeID` (Primary Key)
* `FirstName`
* `LastName`
* `Department`
* `HireDate`
* `Salary`

---

## 🔗 Relationships

* One **Customer → Many Orders**
* Employees are independent (used for salary & department queries)

---

## ⚙️ Key Concepts Covered

### 🔹 Joins

* INNER JOIN → matching records only
* LEFT JOIN → all left + matching right
* RIGHT JOIN → all right + matching left
* FULL OUTER JOIN → simulated using `UNION`

---

### 🔹 Subqueries

* Used to compare values (e.g., above average)
* Nested queries inside WHERE clause

---

### 🔹 Aggregate Functions

* `SUM()`, `AVG()`, `COUNT()`
* Used with `GROUP BY` and `HAVING`

---

### 🔹 Date Functions

* `YEAR()`, `MONTH()`
* `DATEDIFF()`
* `DATE_FORMAT()`

---

### 🔹 String Functions

* `CONCAT()`
* `REPLACE()`
* `UPPER()`, `LOWER()`
* `TRIM()`

---

### 🔹 Window Functions

* `RANK()`
* `SUM() OVER()` for running totals

---

### 🔹 Conditional Logic

* `CASE` statements for:

  * Discounts
  * Salary categorization

---

## 🧪 Sample Use Cases

### ✔ Customers with above-average orders

```sql
SELECT * 
FROM customers 
WHERE CustomerID IN (
    SELECT CustomerID
    FROM orders
    WHERE TotalAmount > (
        SELECT AVG(TotalAmount) FROM orders
    )
);
```

---

### ✔ Employees earning above average salary

```sql
SELECT *
FROM employees
WHERE Salary > (SELECT AVG(Salary) FROM employees);
```

---

### ✔ Running total of orders

```sql
SELECT OrderID, 
       SUM(TotalAmount) OVER (ORDER BY OrderID) AS RunningTotal
FROM orders;
```

---

### ✔ Discount classification

```sql
SELECT OrderID, TotalAmount,
CASE 
    WHEN TotalAmount > 1000 THEN '10% Discount'
    WHEN TotalAmount > 500 THEN '5% Discount'
    ELSE 'No Discount'
END AS Discount
FROM orders;
```

---

## ⚠️ Limitations

* No indexing (performance not optimized)
* Minimal constraints (for learning simplicity)
* FULL OUTER JOIN not natively supported in MySQL

---

## 🚀 Improvements

* Add indexes for faster queries
* Normalize schema further
* Add triggers for automation
* Build frontend/dashboard on top

---

## 🧠 Learning Outcome

After completing this:

* You understand JOIN vs SUBQUERY difference
* You can handle real-world filtering & aggregation
* You know when to use WHERE vs HAVING
* You can write structured, meaningful SQL queries