#!/usr/bin/python3
"""
Display all states from database
"""
import sys
import MySQLdb


"""Connect to MySQL database"""
if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    """run query to retrieve all rows
    form the table"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

for state in states:
    print(state)
