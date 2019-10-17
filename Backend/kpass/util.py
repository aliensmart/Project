from hashlib import sha256,sha512
import random
import requests
import bcrypt



def hash_password(password, salt):
    """ converts a plain-text password to a bcrypt hashed version and random salt, 
    for database storage and lookup """
    passw = password.encode()
    hashed = bcrypt.hashpw(passw, salt)
    return hashed


def random_api_key(length=15):
    seed = (str(random.random()) + str(random.random())).encode()

    hasher = sha512()
    hasher.update(seed)
    output = hasher.hexdigest()
    return output[:length]

    

# if __name__ == "__main__":
#     print(get_price('aapl'))
#     print(hash_password("Password"))
