# Write your MySQL query statement below


WITH new as(SELECT player_id, event_date, MIN(event_date) as first_date
FROM Activity
GROUP BY player_id)


SELECT ROUND(COALESCE(SUM(CASE WHEN DATEDIFF(a.event_date, n.first_date) = 1 THEN 1 END) / COUNT(DISTINCT a.player_id), 0), 2) as fraction
FROM Activity a
JOIN new n
ON a.player_id = n.player_id