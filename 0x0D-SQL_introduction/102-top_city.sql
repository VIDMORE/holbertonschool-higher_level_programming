-- Printing all Dbs in my workspace
-- because mysql the best!

SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
