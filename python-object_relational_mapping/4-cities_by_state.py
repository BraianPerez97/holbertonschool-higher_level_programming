#!/usr/bin/python3
"""List cities by states"""

import sys
from sys import argv
import MySQLdb

if __name__ == '__main__':
    state_names = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, \
                state.name FROM cities "
                "JOIN states ON cities.state_id = states.state_id"
                "ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
