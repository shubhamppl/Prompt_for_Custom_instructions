 --the percentage of employees in each intake group who have scored 45 or more in the SQL assessmen
SELECT Intake, (COUNT(CASE WHEN Score >= 45 THEN 1 END) / COUNT(*)) * 100 AS Percentage
FROM musigma_5qluo_RecentIntakes
GROUP BY Intake;
---- You can use the following SQL query to list the books that have the same genre as the book(s) with the highest price in each genre:
WITH MaxPricePerGenre AS (
    SELECT Genre, MAX(Price) AS MaxPrice
    FROM musigma_5qluo_Library
    GROUP BY Genre
) SELECT l.Title, l.Genre
FROM musigma_5qluo_Library l
JOIN MaxPricePerGenre m
ON l.Genre = m.Genre AND l.Price = m.MaxPrice;

---- find the customer who made the largest single purchase:
SELECT customer_id, order_id, total_price
FROM musigma_5qluo_orders
WHERE total_price = (
    SELECT MAX(total_price) 
    FROM musigma_5qluo_orders
);


-- the most books in the library from the table "musigma_5qluo_Library" with the column name "Author
SELECT Author
FROM musigma_5qluo_Library
GROUP BY Author
ORDER BY COUNT(*) DESC
LIMIT 1;

---mcq---
--Consider a table named "Orders" with columns "OrderDate" and "TotalAmount" What SQL query retrieves the average total order amount for each day of the week (e.g.. Monday, Tuesday, etc.)?
--O Other answer
-O SELECT DAYNAME(OrderDate) AS DayOfWeek, AVG(TotalAmount) FROM Orders GROUP BY DayOfWeek
--O SELECT DATEPART(WEEKDAY, OrderDate) AS DayOfWeek, AVG(TotalAmount) FROM Orders GROUP BY DayOfWeek O SELECT TO CHAR(OrderDate, 'Day') AS DayOfWeek, AVG(TotalAmount) FROM Orders GROUP BY DayOfWeek
--Which option is correct option tell number 
2222222
--Consider a table named "Sales" with columns "ProductID "SaleDate," and "Revenue." What SQL query retrieves the product that generated the highest total revenue on the most recent sale date?

--O SELF ProductID, MAX(Revenue) FROM Sales WHERE SaleDate= (SELECT MAX(SaleDate) FROM Sales)

--SELECT ProductID, SUM(Revenue) AS TotalRevenue FROM Sales GROUP BY ProductID HAVING SaleDate= (SELECT MAX(SaleDate) FROM Sales) ORDER BY TotalRevenue DESC LIMIT 1

--O SELECT ProductID, SUM(Revenue) AS TotalRevenue FROM Sales GROUP BY ProductID HAVING SaleDate= MAX(SaleDate) ORDER BY TotalRevenue DESC LIMIT 1

SELECT ProductID, SUM(Revenue) AS TotalRevenue FROM Sales WHERE SaleDate= (SELECT MAX(SaleDate) FROM Sales) GROUP BY ProductID ORDER BY Total Revenue DESC LIMIT 1
Which option is correct 


3333333333
--Given a table named "Employees with columns "EmployeelD: "Salary" and "Department: what SQL query reve the top-earning employee in each department?

--O SELECT DepartmentID, Salary FROM Employees WHERE Salary MAX(Salary) GROUP BY Department

--O SELECT Department, Employee Salary FROM Employees WHERE (DepartmentID Salary) IN (SELECT Department MAX(Salary) FROM Employens GROUP BY DepartmentID)

SELECT DepartmentID, EmployeeID, Salary FROM Employees WHERE (Departmentio, Salary) IN (SELECT DepartmentID, MAX(Salary) FROM Employees GROUP BY DepartmentID) GROUP BY Department

--SLECT DepartmentID, EmployeeID, Salary FROM Employees WHERE (DepartmentID, Salary) IN (SELECT

--DepartmentID, MAX(Salary) FROM Employees GROUP BY Department(t))
--Which one is correct 
4444
--Given a table named "Orders" with columns "OrderDate" and "TotalAmount" what SQL query retrieves the month with the highest total order amount within the last year?

SELECT EXTRACT(MONTH FROM OrderDate) AS Month, SUM(TotalAmount) AS TotalOrderAmount 
FROM Orders WHERE OrderDate > DATE_SUB(NOW(), INTERVAL 1 YEAR) GROUP BY Month ORDER BY TotalOrderAmount DESC LIMIT 1;

--SELECT EXTRACT(MONTH FROM OrderDate) AS Month, SUM(TotalAmount) AS TotalOrder Amount FROM Onders WHERE OrderDate> NOW() INTERVAL 1 year' GROUP BY Month ORDER BY LxalOrder Amount DE LIMIT

--SELECT EXTRACT(MONTH FROM OrderDate) AS Month, SUM(TotalAmount) AS TotalOrderAmount FROM Qu WHERE OrderDate> DATEADD(YEAR, -1, GETDATE()) GROUP BY Month HAVING TotalOrder Amount MAX(TotalOrderAmount
--hit Assessment
--SELECT TO CHAR(OrderDate, MM) AS Month, MAX(SUM(TotalAmount)) FROM Orders WHERE OrderDate-NOW) -INTERVAL 1 year GROUP BY Month

5555
it counts the number of distinct employess in each departmat

Certainly! You can use the following SQL query to find the customers who made purchases every day for a continuous period of at least 3 days and return their `customer_id` and the start date of this continuous purchase period:

```sql
WITH RankedOrders AS (
    SELECT customer_id, purchase_date,
           DATEDIFF(purchase_date, 
                    lag(purchase_date, 1) OVER (PARTITION BY customer_id ORDER BY purchase_date)
                   ) as diff
    FROM musigma_5qluo_orders
)

SELECT customer_id, MIN(purchase_date) AS start_date
FROM (
    SELECT customer_id, purchase_date, 
           SUM(CASE WHEN diff = 1 THEN 1 ELSE 0 END) OVER (PARTITION BY customer_id ORDER BY purchase_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as consecutive_days
    FROM RankedOrders
) t
WHERE consecutive_days = 3
GROUP BY customer_id, DATE_SUB(purchase_date, INTERVAL consecutive_days - 1 DAY);
```

This query will identify the customers who made purchases every day for a continuous period of at least 3 days and provide their `customer_id` along with the start date of the continuous purchase period.
