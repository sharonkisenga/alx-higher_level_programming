#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if (state_name == row[1]):
            print(row)
