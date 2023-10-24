
In--this MySQL challenge, your query should return all the people who report to either Jenny Richards    *
* --or have a NULL value in ReportsTo. The rows should be ordered by Age. Your query should also add a      *
* --column at the end with a title of Boss Title where the value is either None or CEO.     
SELECT FirstName,LastName,ReportsTo,Position,Age,
CASE WHEN ReportsTo = 'Jenny Richards' THEN 'CEO' ELSE 'None' END AS BossTitle
FROM maintable_WD9RV
WHERE ReportsTo = 'Jenny Richards' OR ReportsTo IS NULL
ORDER BY Age;
                                                                                             
--In this MySQL challenge, your query should return the information for the employee with   *
-- * the third highest salary. Write a query that will find this employee and return that row, *
-- * but then replace the DivisionID column with the corresponding DivisionName from the table *
-- * cb_companydivisions. You should also replace the ManagerID column with the ManagerName if

 *       | 222	 | Mark Red      | Sales	|    Susan Wall	     | 86000 	     |       *
 *       +-------+---------------+--------------+--------------------+---------------+       *


SELECT m.ID,m.Name,d.DivisionName AS DivisionName, 
    IFNULL(mr.Name, 'No Manager') as ManagerName, 
    m.Salary 
FROM maintable_M3LJZ as m
JOIN cb_companydivisions d ON m.DivisionID = d.id
LEFT JOIN maintable_M3LJZ mr ON m.ManagerID = mr.ID
WHERE m.Salary = (SELECT DISTINCT Salary FROM maintable_M3LJZ
    ORDER BY Salary DESC
    LIMIT 2, 1);
---------------------------------OOOOOORRRRRRRRR------------------------------------------------------
SELECT 
maintable_M3LJZ.ID,  maintable_M3LJZ.Name, cb_companydivisions.DivisionName AS DivisionName,
        t.Name AS ManagerName, maintable_M3LJZ.Salary FROM maintable_M3LJZ
JOIN cb_companydivisions ON cb_companydivisions.id = maintable_M3LJZ.DivisionID
JOIN ( SELECT Name,  ID FROM maintable_M3LJZ) AS t ON t.ID = maintable_M3LJZ.ManagerID
WHERE Salary = (SELECT MIN(Salary) FROM (SELECT * FROM maintable_M3LJZ 
                            ORDER BY salary DESC LIMIT 3) AS x)
--In this MySQL challenge, your query should return the names of the people who are reported*
--* to (excluding null values) the number of members that report to them, and the average the *
--* number of members that report to them, and the average age of those members as an integer *

 *                        +-----------------+------------+------------+                      *
 *                        | Bob Boss        | 2          | 24         |                      *

SELECT  ReportsTo,COUNT(ReportsTo) AS Members,
        CEIL(AVG(AGE)) AS `Average Age`
FROM maintable_L99ON WHERE ReportsTo IS NOT NULL
GROUP BY ReportsTo ORDER BY ReportsTo
--
--In this MySQL challenge, your query should return the vendor information along with *
-- * the values from the table cb_vendorinformation. You should combine the values of the*
-- * two tables based on the GroupID column. The final query should only print out the   *
-- * GroupID, CompanyName, and final count of all rows that are grouped into each company*
-- * name under a column titled Count. The output table should be then sorted by the     *
-- * Count column and then sorted by GroupID so that a higher number appears first.
 *                       | GroupID | CompanyName         | Count |                     *
 *                       +---------+---------------------+-------+                     *
 *                       |       27| Machinx             |      1|                     *


SELECT 
    maintable_V47CA.GroupID,
    cb_vendorinformation.CompanyName,
    COUNT(maintable_V47CA.GroupID) AS `Count`
FROM 
    maintable_V47CA
JOIN cb_vendorinformation ON cb_vendorinformation.GroupID = maintable_V47CA.GroupID
GROUP BY
    maintable_V47CA.GroupID,
    cb_vendorinformation.CompanyName
ORDER BY 
    COUNT(maintable_V47CA.GroupID),
    maintable_V47CA.GroupID


--        your query should return the vendor information along with the values from the table cb_vendorinformation.                      *
--       You should combine the values of the two tables based on the GroupID column.                                                    *
--       The final query should consolidate the rows to be grouped by FirstName,                                                         *
--      and a Count column should be added at the end that adds up the number of times that person shows up in the table.               
*                     |      35 |    Daniel  | Knolle    | Manager    | 39765        | Shipping & Co.      |     6  |                    *
*                     +---------+------------+-----------+------------+--------------+---------------------+--------+                    *
*                     |      35 |    Arnold  | Sully     | Manager    | 48507        | Shipping & Co.      |     6  |                    *
--

SELECT 
        * 
FROM 
(
        SELECT 
                main_table.GroupID,
                main_table.FirstName,
                main_table.LastName,
                main_table.Job,
                main_table.ExternalID,
                cb_vendorinformation.CompanyName,
        ( SELECT COUNT(*) FROM maintable_J22DJ AS sub_table WHERE main_table.FirstName = sub_table.FirstName ) AS Count
        FROM 
                maintable_J22DJ AS main_table
        JOIN cb_vendorinformation ON cb_vendorinformation.GroupID = main_table.GroupID
        GROUP by FirstName, LastName
) AS SubQuery
ORDER BY SubQuery.COUNT, SubQuery.CompanyName, SubQuery.FirstName DESC


------------------------------salary difference-------------------------------------
WITH cte AS ( SELECT  Name, 
        dept AS department, salary, 
        MAX(salary) OVER(PARTITION BY dept) AS maxsalary 
    FROM  table_name)
SELECT  Name, department, 
    (maxsalary - salary) AS salary_difference 
FROM  cte 
WHERE department = 'IT';

--------------------- Youngest employee ---------------------------------------
SELECT  name, age 
FROM  table_name
ORDER BY age 
LIMIT 3;
---------
SELECT    CASE
WHEN login_time <= 15 THEN '15-30'
WHEN logout_time <= 30 THEN '38-45'
ELSE '45+'
END AS session_duration,
COUNT(*) AS number_of_sessions
FROM musigma_5qluo_loginfo
GROUP BY session_duration;

--- * In this MySQL challenge, the table provided shows all new users signing up on a specific  *
---- * date in the format YYYY-MM-DD. Your query should output the change from one month to the  *
--- * next. Because the first month has no preceding month, your output should skip that row.   * 
---* Your output should look like the following table. SELECT Month, MonthToMonthChange
 *      | ID            | DateJoined    |                                                    *
 *      +---------------+---------------+                                                    *
 *      | 2343434	| 2017-01-06    |                                                    
SELECT
    MONTHNAME(Date1) AS Month,
    Date1 - Previous AS MonthToMonthChange
FROM
(SELECT DateJoined AS Date1, @prev AS Previous, @prev := DateJoined AS dummy
    FROM  maintable_O9AAP,(SELECT @prev := NULL) r
    ORDER BY DateJoined) AS sub
WHERE Previous IS NOT NULL;
----------- or with lag-----------------------
SELECT MONTHNAME(Date1) AS Month,
    Date1 - LAG(Date1) OVER (ORDER BY DateJoined) AS MonthToMonthChange
FROM(SELECT COUNT(DateJoined) AS Date1, DateJoined
    FROM  maintable_O9AAP
    GROUP BY MONTH(DateJoined)
    ORDER BY DateJoined) AS sub
WHERE LAG(Date1) OVER (ORDER BY DateJoined) IS NOT NULL;
