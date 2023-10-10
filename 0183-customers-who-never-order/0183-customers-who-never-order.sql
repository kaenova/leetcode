# Write your MySQL query statement below
SELECT name as "Customers"
FROM Customers C
WHERE C.id NOT IN (
    SELECT DISTINCT customerID as "id" FROM ORDERS 
)
