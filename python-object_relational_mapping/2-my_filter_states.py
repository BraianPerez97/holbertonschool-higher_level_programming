#!/usr/bin/python3
"""lists states
"""

import MySQLdb
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name_searched = sys.argv[4]
    port = 3306

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        db=db,
        port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE NAME LIKE '{}' ORDER BY states.id;".format)
    states = cur.fetchall()

    for state in states:
        print(state)
