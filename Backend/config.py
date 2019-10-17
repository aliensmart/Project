import os

SALT = "this is secret to everybody"

DIR = os.path.join(os.path.dirname(__file__), 'data')
DBFILENAME = "kpass.db"
DBPATH = os.path.join(DIR, DBFILENAME)