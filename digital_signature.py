from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Message to sign
message = b"This message is authentic."

# Create hash of the message
h = SHA256.new(message)

# Sign the hash
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

# Verify the signature
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature is valid!")
except (ValueError, TypeError):
    print("Signature is invalid!")
