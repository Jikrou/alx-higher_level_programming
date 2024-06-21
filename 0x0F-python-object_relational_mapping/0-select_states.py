#!/usr/bin/python3
""" Lists all the states from the the database """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()
