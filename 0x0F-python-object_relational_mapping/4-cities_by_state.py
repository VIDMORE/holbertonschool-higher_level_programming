#!/usr/bin/python3
"""This module defines a simple query """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    passw = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passw, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states\
                 ON cities.state_id=states.id ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
