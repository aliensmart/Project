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
                email VARCHAR UNIQUE NOT NULL,
                username VARCHAR(16) NOT NULL,
                password_hash VARCHAR(128),
                salt VARCHAR UNIQUE,
                api_key VARCHAR UNIQUE,
                user_id VARCHAR UNIQUE,
                UNIQUE(username)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="passwords"))

        SQL = """CREATE TABLE passwords(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR,
                username VARCHAR(16) NOT NULL,
                password_hash VARCHAR(128) NOT NULL,
                salt VARCHAR UNIQUE,
                site_name VARCHAR,
                url VARCHAR UNIQUE NOT NULL,
                account_pk INTEGER,
                FOREIGN KEY(account_pk) REFERENCES accounts(pk)
                

            );"""

        cur.execute(SQL)


