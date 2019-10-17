import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "kpass.db"
DBPATH = os.path.join(DIR, DBFILENAME)


def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="accounts"))

        SQL = """CREATE TABLE accounts(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR UNIQUE,
                username VARCHAR(16) NOT NULL,
                password_hash VARCHAR(128),
                api_key VARCHAR UNIQUE,
                UNIQUE(username)
            );"""

        cur.execute(SQL)


