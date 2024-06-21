#!/usr/bin/python3
""" Script that lists all states that starts with N """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    names = cur.fetchall()

    for n in names:
        print(n)

    cur.close()
    db.close()
