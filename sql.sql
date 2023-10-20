 
 *       | 222	 | Mark Red      | Sales	|    Susan Wall	     | 86000 	     |       *
 *       +-------+---------------+--------------+--------------------+---------------+       *


SELECT 
    m.ID, 
    m.Name, 
    d.DivisionName AS DivisionName, 
    IFNULL(mr.Name, 'No Manager') as ManagerName, 
    m.Salary 
FROM maintable_M3LJZ m
JOIN cb_companydivisions d ON m.DivisionID = d.id
LEFT JOIN maintable_M3LJZ mr ON m.ManagerID = mr.ID
WHERE m.Salary = (
    SELECT DISTINCT Salary
    FROM maintable_M3LJZ
    ORDER BY Salary DESC
    LIMIT 2, 1
);

 *                        +-----------------+------------+------------+                      *
 *                        | Bob Boss        | 2          | 24         |                      *

SELECT  ReportsTo,COUNT(ReportsTo) AS Members,
        CEIL(AVG(AGE)) AS `Average Age`
FROM maintable_L99ON        
WHERE ReportsTo IS NOT NULL
GROUP BY ReportsTo
ORDER BY ReportsTo

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


------------------------------
WITH cte AS ( SELECT  Name, 
        dept AS department, salary, 
        MAX(salary) OVER(PARTITION BY dept) AS maxsalary 
    FROM  table_name)
SELECT  Name, department, 
    (maxsalary - salary) AS salary_difference 
FROM  cte 
WHERE department = 'IT';

-- Youngest employee
SELECT  name, age 
FROM  table_name
ORDER BY age 
LIMIT 3;

