-- Printing all Dbs in my workspace
-- because mysql the best!

SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
