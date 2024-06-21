#!/usr/bin/python3
""" a safe script that takes an argument and displays all
    the values in the states table. """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    in_str: str = sys.argv[4]
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (in_str,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    db.close()
