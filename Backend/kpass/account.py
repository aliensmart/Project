from kpass.orm import ORM
from .util import hash_password, get_price
import random


class Account(ORM):

    tablename = "accounts"
    fields = ['username', 'password_hash', 'email', 'api_key']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.email = kwargs.get("email")
        self.api_key = kwargs.get("api_key")

    @classmethod
    def login(cls, username, password):
        return cls.one_from_where_clause("WHERE username=? AND password_hash=?",
                                        (username, hash_password(password)))

    def set_password(self, password):
        self.password_hash = hash_password(password)
    
    def generate_api_key(self):
        """
        This method sets the  self.api_key 
        property to a random string of at least 20 
        numbers or characters

        """
        start = 10**19
        end = (10**20)-1
       
        new_api = random.randint(start,end)
        self.api_key = str(new_api)
        return self.api_key

    def get_api(self):
        return self.api_key

    # classmethod of Account called api_authenticate
    @classmethod
    def api_authenticate(cls, api_key):
        return cls.one_from_where_clause("WHERE api_key=?",
                                        (api_key,))


