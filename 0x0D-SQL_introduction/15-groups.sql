-- Printing all Dbs in my workspace
-- because mysql the best!

SELECT score, count(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
