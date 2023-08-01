#!/usr/bin/python3
"""List cities by states"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, \
                state.name FROM cities "
                "JOIN states ON cities.state_id = states.state_id"
                "ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
