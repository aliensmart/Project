import os
import time
# from app.orm import ORM
from kpass import Account, ORM

DIR = os.path.dirname(__file__)
DBFILENAME = 'kpass.db'
DBPATH = os.path.join(DIR, DBFILENAME)


def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    
    mike_bloom = Account(username='mike_bloom', password="password", email='email@email.com')
    mike_bloom.set_password("password")
    mike_bloom.save()
