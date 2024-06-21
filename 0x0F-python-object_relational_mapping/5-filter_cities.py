#!/usr/bin/python3
""" list all the cities of the given state """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    str_q = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (str_q,))

    citys = cur.fetchall()
    r = list(c[0] for c in citys)
    print(*r, sep=", ")

    cur.close()
    db.close()
