#!/usr/bin/python3
"""List all states matching the name"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM state WHERE \
                NAME = %s ORDER BY states.id;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
