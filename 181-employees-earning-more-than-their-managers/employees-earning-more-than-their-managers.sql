# Write your MySQL query statement below
select E1.name as Employee from Employee E1 LEFT join  Employee E2 on E1.ManagerId = E2.Id where E1.salary > E2.salary
