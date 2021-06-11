# Hashing Passwords With pbkdf2_hmac

PBKDF2 is a key derivation function where the user can set the computational cost; this aims to slow down the calculation of the key to making it more impractical to brute force. In usage terms, it takes a password, salt and a number of iterations to produce a certain key length which can also be compared to a hash as it is also a one-way function.

PBKDF2_HMAC is an implementation of the PBKDF2 key derivation function using HMAC as pseudorandom function. pbkdf2_hmac can be found in the hashlib library (which comes with Python) and is in Python 3.4 and above. pbkdf2_hmac takes five parameters:
- **hash_name**: hash digest algorithm for HMAC
- **password**: the password being turned into the key
- **salt**: a randomly generated salt
- **iterations**: iterations in the calculation (higher means more computation required)
- **dklen**: length of the output key (not required)

## Generating a Salt
Before generating the key using pbkdf2_hmac, you need to generate a random salt. Salts make the search space larger in the case of brute-forcing and adds difficulty for rainbow tables; using a salt only requires you to do a little more work and store an extra random byte sequence.

