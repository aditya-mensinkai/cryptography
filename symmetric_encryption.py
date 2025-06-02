from cryptography.fernet import Fernet

# Generate a random symmetric key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Plaintext message
plaintext = b"This is a secret message."

# Encrypt the message
ciphertext = cipher_suite.encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = cipher_suite.decrypt(ciphertext)
print(f"Decrypted Message: {decrypted_message.decode()}")