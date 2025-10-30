# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary
FROM Employee e
LEFT JOIN Department d 
    ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT em.salary)
    FROM Employee em
    WHERE em.salary > e.salary 
      AND em.departmentId = e.departmentId
) < 3
ORDER BY e.departmentId, e.salary DESC;

-- Group by d.name 
-- Order by e.salary 
-- DESC Limit 3