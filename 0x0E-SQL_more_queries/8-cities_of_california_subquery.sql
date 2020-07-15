-- Printing all Dbs in my workspace
-- because mysql is the best!

SELECT
       id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name='California')
ORDER BY id ASC;
