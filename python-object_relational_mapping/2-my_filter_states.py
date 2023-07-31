#!/usr/bin/python3
"""lists states
"""


import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databases = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=databases,
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE NAME LIKE '{}' \
            ORDER BY states.id;".format(state_name_searched))
    states = cur.fetchall()

    for state in states:
        print(state)
