#!/usr/bin/python3
"""Relational mapping
"""

import sys
import MySQLdb

"""Connect to MySQL database"""
if __name__ == '__main__':
    db = MySQLdb.connect(
        host= 'localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    """run query to retrieve all rows
    form the table"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

        cur.close()
        db.close()
