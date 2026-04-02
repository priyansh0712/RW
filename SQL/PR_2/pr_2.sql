-- 1. Customer table

CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    RegistrationDate DATE
);

INSERT INTO customers (CustomerID, FirstName, LastName, Email, RegistrationDate) VALUES
(1, 'John', 'Doe', ' john.doe@email.com ', '2022-03-15'),
(2, 'Jane', 'Smith', ' jane.smith@email.com ', '2021-11-02'),
(3, 'Mike', 'Brown', ' mike.b@email.com ', '2023-01-10'),
(4, 'Emma', 'Wilson', ' emma.w@email.com ', '2022-07-25'),
(5, 'Chris', 'Taylor', ' chris.t@email.com ', '2023-05-18');

-- 2. Orders table

CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

INSERT INTO orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(101, 1, '2023-07-01', 150.50),
(102, 2, '2023-07-03', 200.75),
(103, 3, '2023-07-05', 600.00),
(104, 1, '2023-07-07', 1200.00),
(105, 4, '2023-07-10', 450.00),
(106, 5, '2023-07-12', 800.00);

-- 3. Employees table

CREATE TABLE employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Department VARCHAR(50),
    HireDate DATE,
    salary DECIMAL(10, 2)
)

INSERT INTO employees (EmployeeID, FirstName, LastName, Department, HireDate, Salary) VALUES
(1, 'Mark', 'Johnson', 'Sales', '2020-01-15', 50000),
(2, 'Susan', 'Lee', 'HR', '2021-03-20', 55000),
(3, 'David', 'Clark', 'IT', '2019-06-10', 70000),
(4, 'Nina', 'Patel', 'IT', '2022-02-01', 80000),
(5, 'Raj', 'Shah', 'Sales', '2021-08-12', 45000);

----------------------------------------------------------------------------------------------

SELECT e.*,o.* from customers e INNER JOIN orders o ON e.CustomerID = o.CustomerID;
SELECT c.*,O.* from customers c LEFT join orders o ON c.`CustomerID`=o.`CustomerID`

SELECT o.*,c.* from orders o RIGHT join customers c ON o.`CustomerID`=c.`CustomerID`

SELECT c.*,O.* from customers c LEFT join orders o ON c.`CustomerID`=o.`CustomerID` UNION SELECT o.*,c.* from orders o RIGHT join customers c ON o.`CustomerID`=c.`CustomerID`

SELECT * from customers WHERE `CustomerID` IN (SELECT `CustomerID` from orders where `TotalAmount`> (SELECT AVG(`TotalAmount`) from orders));

SELECT * from employees where salary > (select AVG(salary) from employees)

SELECT YEAR(OrderDate) as OrderYear,MONTH(OrderDate) as Month from orders

SELECT OrderID,DATEDIFF(NOW(), OrderDate) as days from orders

SELECT OrderID, DATE_FORMAT(OrderDate, '%d-%m-%y') from orders

SELECT CustomerID, CONCAT(FirstName, " ", LastName) as FullName from customers

SELECT CustomerID,REPLACE(`FirstName`,'John','Jonathan') from customers

SELECT CustomerID,UPPER(FirstName),LOWER(LAstName) from customers

SELECT CustomerID,TRIM(Email) from customers

SELECT OrderID,`TotalAmount`,SUM(`TotalAmount`) OVER (ORDER BY `OrderID`) as RunningTotal FROM orders 

SELECT OrderID, TotalAmount, RANK() OVER(order BY `TotalAmount` DESC) from orders

SELECT OrderID, TotalAmount, case WHEN TotalAmount > 1000 THEN TotalAmount*0.01 WHEN TotalAmount > 500 THEN `TotalAmount`*0.05 Else TotalAmount*0.0 END as Discount from orders

SELECT *, case WHEN Salary > 75000 THEN 'High' WHEN Salary > 50000 THEN 'Medium' Else 'Low' END as SalaryRange from employees
