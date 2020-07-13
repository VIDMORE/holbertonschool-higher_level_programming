-- Printing all Dbs in my workspace
-- because mysql the best!

SELECT DISTINCT(state), MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;

