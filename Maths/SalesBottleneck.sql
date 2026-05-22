SELECT * from regionalsales2025

-- 1. Monthly trend of sales across all regions
SELECT MONTH(Date) AS MonthNo,MONTHNAME(Date) AS MonthName,SUM(TotalAmount) AS TotalSales FROM RegionalSales2025 GROUP BY MONTH(Date), MONTHNAME(Date)
ORDER BY MonthNo;

-- 2. Percentage of cancelled and returned orders per region
SELECT Region,ROUND(SUM(CASE 
    WHEN OrderStatus IN ('Cancelled','Returned') THEN 1  
    ELSE 0 END)*100.0/COUNT(*),2) AS LossPercentage from regionalsales2025 GROUP BY Region;

-- 3. Identify Top-3 products with most revenue loss
SELECT ProductName,SUM(TotalAmount) AS RevenueLoss FROM RegionalSales2025 WHERE OrderStatus IN ('Cancelled','Returned') GROUP BY ProductName ORDER BY RevenueLoss DESC LIMIT 3;

-- 4. Average order value by product category
SELECT Category,ROUND(AVG(TotalAmount),2) AS AvgOrder FROM RegionalSales2025 GROUP BY Category;

--5.Top 5 performin sales agent
SELECT SalesAgent,sum(TotalAmount) as TotalSales from regionalsales2025 GROUP BY `SalesAgent` ORDER BY TotalSales DESC LIMIT 5;

--6. Category-wise total sales and contibution to grant total
SELECT Category,SUM(TotalAmount) AS CategorySales,ROUND(SUM(TotalAmount) * 100 /(SELECT SUM(TotalAmount)FROM RegionalSales2025),2) AS ContributionPercent FROM RegionalSales2025 GROUP BY Category;

--7. List customers with highest frequency of returns(>= 3 times)
SELECT CustomerID,COUNT(*) AS ReturnCount FROM RegionalSales2025 WHERE OrderStatus='Returned'GROUP BY CustomerID HAVING COUNT(*) >= 3
ORDER BY ReturnCount DESC;