import os
import hashlib

salt=os.urandom(32)
# os.urandom function, used here for generating salts; 
# returns random bytes suitable for cryptographic use 

# Example for hash generation
key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    'mypassword'.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000, # It is recommended to use at least 100,000 iterations of SHA-256 
    dklen=128 # Get a 128 byte key
)

# Store it as
storage = salt + key 

# Getting the values back out
salt_from_storage = storage[:32] # 32 is the length of the salt
key_from_storage = storage[32:]