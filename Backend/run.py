#! /usr/bin/env python3
from kpass import Account
from kpass import ORM
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'kpass.db')
ORM.dbpath = DBPATH
# Account.dbpath = DBPATH


