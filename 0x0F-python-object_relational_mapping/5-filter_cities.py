#!/usr/bin/python3
"""This module defines a simple query """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    passw = argv[2]
    database = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passw, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id",
                (state, ))

    listt = []
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
