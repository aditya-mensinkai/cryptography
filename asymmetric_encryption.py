from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Create cipher object for encryption with public key
recipient_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)

# Encrypt
message = b"Hello, this is a secret!"
ciphertext = cipher_rsa.encrypt(message)

# Create cipher object for decryption with private key
private_key_obj = RSA.import_key(private_key)
cipher_rsa_dec = PKCS1_OAEP.new(private_key_obj)
decrypted = cipher_rsa_dec.decrypt(ciphertext)

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted.decode())
