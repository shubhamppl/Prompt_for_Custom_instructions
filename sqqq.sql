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

---
