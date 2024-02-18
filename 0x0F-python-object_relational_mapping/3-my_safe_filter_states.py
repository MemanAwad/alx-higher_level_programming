#!/usr/bin/python3
""" script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument."""
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
    sql_query = "SELECT * FROM states WHERE name=%s"
    cur.execute(sql_query, (sys.argn[4],))
    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()
