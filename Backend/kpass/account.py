from kpass.orm import ORM
import bcrypt
from .util import hash_password
import random


class Account(ORM):

    tablename = "accounts"
    fields = ['username', 'password_hash', 'salt', 'email', 'api_key']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.email = kwargs.get("email")
        self.api_key = kwargs.get("api_key")
        self.salt = kwargs.get("salt")
        

    @classmethod
    def login(cls, username, password):
        #W
        salt = cls.one_col_from_where_clause("salt", "WHERE username=?", (username,))
        if salt:

            return cls.one_from_where_clause("WHERE username=? AND password_hash=?",
                                        (username, hash_password(password,salt) ))
        else:
            return None

    def set_password(self, password):
        self.salt = bcrypt.gensalt()
        self.password_hash = hash_password(password, self.salt)
    
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


