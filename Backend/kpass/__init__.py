from .account import Account
from .orm import ORM
from .passwords import Passwords

def  setdb(dbpath):
    ORM.dbpath = dbpath