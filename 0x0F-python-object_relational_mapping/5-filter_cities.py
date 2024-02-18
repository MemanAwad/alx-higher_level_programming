#!/usr/bin/python3
""" script that lists take the name of the dtate as an argument
and list all the cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cur = db.cursor()
    sql_query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s\
            ORDER BY cities.id ASC"
    cur.execute(sql_query, (sys.argv[4], ))
    result = cur.fetchall()

    display = []
    for row in result:
        display.append(row[0])
    print(', '.join(display))

    cur.close()
    db.close()
