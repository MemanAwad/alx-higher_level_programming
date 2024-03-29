#!/usr/bin/python3
""" list all states with name staring with N"""
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
    sql_query = "SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC"
    cur.execute(sql_query)
    result = cur.fetchall()
    for row in result:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
