from .orm import ORM
import bcrypt
from .util import hash_password

class Passwords(ORM):
    tablename="passwords"
    fields=["email", "username", "password_hash", "salt", "site_name", "account_pk"]
    
    def __init__(self, **kwargs):
        self.pk = kwargs.get('')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.salt = kwargs.get('salt')
        self.site_name = kwargs.get('site_name')
        self.account_pk = kwargs.get('account_pk')

    
    def set_password(self, password):
        self.salt = bcrypt.gensalt()
        self.password_hash = hash_password(password, self.salt)

    # def set_salt(self):
        