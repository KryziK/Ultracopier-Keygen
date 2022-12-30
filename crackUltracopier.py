# https://github.com/alphaonex86/Ultracopier/blob/280fd21352aea05784c1097348df489210855109/ProductKey.cpp

import hashlib
import secrets
import string

ALPHABET = string.ascii_letters + string.digits + string.punctuation
KEY_LENGTH = 10 # Arbitrary
SALT = "mQcLvEg1HW8JuRXY3BawjSpe"

saltBytes = bytes("mQcLvEg1HW8JuRXY3BawjSpe", 'utf-8')
key = ''

while(True):
    key = ''.join(secrets.choice(ALPHABET) for i in range(KEY_LENGTH))
    keyBytes = bytes(key, 'utf-8')
    h = hashlib.sha224(saltBytes + keyBytes).digest()

    if (h.hex()[0:4] == '0' * 4):
        break

print('Product Key (length ' + str(KEY_LENGTH) + ', no whitespace): ' + key)