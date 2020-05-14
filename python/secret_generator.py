import secrets

import string
import argon2

def random_string(length=24):
    letters = string.ascii_letters
    numbers = string.digits
    return ''.join(secrets.choice(letters+numbers) for i in range(length))


def get_salt(length=24):
    letters = string.ascii_letters
    numbers = string.digits
    salt = ''.join(secrets.choice(letters+numbers) for i in range(length))
    return salt

salt = get_salt(16)
print(salt)
print(argon2.argon2_hash('1234', salt).hex())

