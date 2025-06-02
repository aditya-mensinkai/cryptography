import hashlib
import os

def hash_password_with_salt(password):
    # Generate a random 16-byte salt
    salt = os.urandom(16)

    # Combine salt with the password (convert password to bytes)
    salted_password = salt + password.encode()

    # Create the hash
    hash_digest = hashlib.sha256(salted_password).hexdigest()

    # Return both salt and hash
    return salt, hash_digest

def verify_password(password, salt, stored_hash):
    # Hash the provided password with the stored salt
    salted_password = salt + password.encode()
    hash_digest = hashlib.sha256(salted_password).hexdigest()

    # Compare with stored hash
    return hash_digest == stored_hash

# Example usage
password = "my_secure_password"

# Hash and salt
salt, hash_digest = hash_password_with_salt(password)
print(f"Salt (hex): {salt.hex()}")
print(f"Hashed Password: {hash_digest}")

# Verify password
is_valid = verify_password(password, salt, hash_digest)
print(f"Password valid: {is_valid}")

