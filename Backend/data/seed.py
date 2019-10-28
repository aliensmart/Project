import os
import time
# from app.orm import ORM
from kpass import Account, ORM, Passwords

DIR = os.path.dirname(__file__)
DBFILENAME = 'kpass.db'
DBPATH = os.path.join(DIR, DBFILENAME)


def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    
    mike_bloom = Account(username='mike_bloom', password="password", email='email@email.com')
    mike_bloom.set_password("password")
    mike_bloom.save()

    account_1 = Passwords(email="kaoua121@gmail.com", username="mike_bloom", password="password", site_name="FaceBook", account_pk=1, url="https://www.facebook.com/")
    account_1.set_password("password")
    account_1.save()

    justin_sarra = Account(username='justinSarra', password="password", email='email1@email.com')
    justin_sarra.set_password("password")
    justin_sarra.save()

    account_2 = Passwords(email="justPerf@gmail.com", username="mike_bloom", password="password", site_name="FaceBook", account_pk=2, url="https://www.facebook.com/")
    account_2.set_password("password")
    account_2.save()
