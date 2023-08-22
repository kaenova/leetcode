# Write your MySQL query statement below
SELECT a.email
FROM (
    SELECT email, count(email) "ce" FROM PERSON WHERE email is not NULL GROUP BY email
) a
WHERE a.ce >= 2
