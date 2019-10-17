from .account import Account
from .orm import ORM

def  setdb(dbpath):
    ORM.dbpath = dbpath