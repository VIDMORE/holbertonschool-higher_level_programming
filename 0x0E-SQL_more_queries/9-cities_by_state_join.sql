-- Printing all Dbs in my workspace
-- because mysql is the best!

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
