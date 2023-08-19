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
    cur.execute("SELECT cities.name\
         FROM states\
         INNER JOIN cities ON states.id = cities.state_id\
         WHERE states.name=%s\
         ORDER BY cities.id ASC", [name])
    query_rows = cur.fetchall()

    print(", ".join([city[0] for city in query_rows]))

    cur.close()
    conn.close()
