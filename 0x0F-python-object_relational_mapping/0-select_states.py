#!/usr/bin/python3
""" script to list all the states from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql_query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(sql_query)
    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()
