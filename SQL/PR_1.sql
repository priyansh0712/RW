CREATE TABLE customer(customer_id int,name varchar(50),email VARchar(50),address varchar(100))
INSERT INTO customer (customer_id, name, email, address) VALUES(1, 'John Smith', 'john@example.com', 'New York, USA'),(2, 'Sarah Johnson', 'sarah@example.com', 'London, UK'),(3, 'Michael Brown', 'michael@example.com', 'Toronto, Canada'),(4, 'Emma Davis', 'emma@example.com', 'Sydney, Australia'),(5, 'David Miller', 'david@example.com', 'Berlin, Germany');
SELECT * from customer
UPDATE customer set address='india' WHERE customer_id = 1
DELETE from customer where customer_id=2
SELECT * from customer WHERE name='Emma Davis'

-- 2.

CREATE TABLE orders (
    OrderID INT primary key,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES customer(customer_id)
);
INSERT INTO orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2025-03-01', 60000.00),
(2, 2, '2025-03-02', 2000.00),
(3, 3, '2025-03-03', 1500.00),
(4, 1, '2025-03-04', 12000.00),
(5, 4, '2025-03-05', 2500.00);
SELECT * from orders where CustomerID = 1
UPDATE orders set TotalAmount = 70000.00 WHERE OrderID = 2
DELETE FROM orders WHERE OrderID = 3
SELECT TOP 30 * from orders ORDER BY OrderDate DESC;
SELECT MAX(TotalAmount) as max, MIN(TotalAmount) as min, AVG(TotalAmount) as avg from orders;

-- 3.

CREATE Table products(product_id int,name VARCHAR(50),price DECIMAL(10,2),stock int)
INSERT INTO products (product_iD, name, price, stock) VALUES
(1, 'Laptop', 55000.00, 10),
(2, 'Mouse', 500.00, 50),
(3, 'Keyboard', 1500.00, 30),
(4, 'Monitor', 12000.00, 15),
(5, 'Headphones', 2000.00, 25);
SELECT * from products ORDER BY price DESC
update products set price = 10000.00 WHERE name = 'Monitor'
DELETE from products WHERE stock = 0
SELECT * from products where price< 150000.00 AND price>500.00
SELECT MAX(price) as max,MIN(price) as min from products

-- 4.

CREATE TABLE order_details (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SubTotal DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

INSERT INTO order_details (OrderDetailID, OrderID, ProductID, Quantity, SubTotal) VALUES
(1, 1, 1, 1, 55000.00),
(2, 1, 2, 2, 1000.00),
(3, 2, 3, 1, 1500.00),
(4, 3, 2, 3, 1500.00),
(5, 4, 4, 1, 12000.00);

SELECT * FROM order_details WHERE OrderID = 1;
SELECT SUM(SubTotal) AS total_revenue FROM order_details;
SELECT TOP 3 ProductID, SUM(Quantity) AS total_quantity FROM order_details GROUP BY ProductID ORDER BY total_quantity DESC;
SELECT ProductID, COUNT(*) AS times_sold
FROM order_details
WHERE ProductID = 2
GROUP BY ProductID;