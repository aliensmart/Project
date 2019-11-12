from hashlib import sha256,sha512
import random
import requests
import bcrypt



#-------------------Hashing Password-----------------------------------------------------------------------------------------------------------------
def hash_password(password, salt):
    """ converts a plain-text password to a bcrypt hashed version and random salt, 
    for database storage and lookup """
    passw = password.encode()
    hashed = bcrypt.hashpw(passw, salt)
    return hashed

#---------------------APi Creation------------------------------------------------------------------------------------------------------------------------
def random_api_key(length=15):
    seed = (str(random.random()) + str(random.random())).encode()
    hasher = sha512()
    hasher.update(seed)
    output = hasher.hexdigest()
    return output[:length]