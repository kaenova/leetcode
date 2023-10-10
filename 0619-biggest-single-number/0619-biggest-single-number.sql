# Write your MySQL query statement below
SELECT MAX(A.num) as "num"
FROM (
    SELECT num, COUNT(num) as "count" FROM MyNumbers GROUP BY num
) A
WHERE A.count = 1
