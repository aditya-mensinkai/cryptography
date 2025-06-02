import hmac
import hashlib

# Secret key (should be securely stored and shared)
secret_key = b'super_secret_key'

# Message to authenticate
message = b'This is a sensitive message.'

# Create HMAC object using SHA-256
hmac_obj = hmac.new(secret_key, message, hashlib.sha256)

# Get the hexadecimal digest
hmac_digest = hmac_obj.hexdigest()

print(f"Message: {message.decode()}")
print(f"HMAC: {hmac_digest}")

# Verifying the message
# Let's assume this is the received HMAC
received_hmac = hmac_digest

# Receiver recomputes the HMAC
recomputed_hmac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

if hmac.compare_digest(received_hmac, recomputed_hmac):
    print("Message is authentic and untampered.")
else:
    print("Message integrity check failed!")

