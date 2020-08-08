#!/usr/bin/python3
"""This module defines a simple query """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    passw = argv[2]
    database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passw, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
