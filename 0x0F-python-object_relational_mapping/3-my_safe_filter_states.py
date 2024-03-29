#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id."""
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(port=3306,
                           host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    sp = sys.argv[4].split("'")
    name = sp[0]
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
                ORDER BY id ASC;", [name])
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
