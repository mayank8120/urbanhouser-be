import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Define parameters (adjust as needed)
iterations = 390000  # Number of iterations
salt_length = 16  # Bytes


def hash_password(password):
    # Generate random salt
    salt = os.urandom(salt_length)

    # Create the PBKDF2HMAC object
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Output length in bytes
        salt=salt,
        iterations=iterations,
    )

    # Derive the key
    key = kdf.derive(password.encode())

    # Store the salt and hashed key securely
    return salt + key


def verify_password(plain_password, stored_password):
    salt, hashed_key = stored_password[:salt_length], stored_password[salt_length:]

    # Ensure salt is bytes
    salt = salt if isinstance(salt, bytes) else salt.encode()

    # Derive the key from the provided password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Output length in bytes
        salt=salt,
        iterations=iterations,
    )
    derived_key = kdf.derive(plain_password.encode())

    # Use constant-time comparison
    return constant_time_compare(hashed_key, derived_key)


def constant_time_compare(val1, val2):
    # Implement constant-time comparison to avoid timing attacks
    result = 0
    for x, y in zip(val1, val2):
        result |= x ^ y
    return result == 0
