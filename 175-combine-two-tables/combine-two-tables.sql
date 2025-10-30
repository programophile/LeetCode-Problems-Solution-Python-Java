# Write your MySQL query statement below
Select p.firstName,p.lastName , a.city,a.state FROM Person p LEFT JOIN Address a on 
p.personId = a.PersonId