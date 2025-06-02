import hashlib

# Input data
data = "Hello, this is hashing!"

print(f"Input Data: {data}")
print("=" * 50)

# MD5 Hash (128-bit)
md5_hash = hashlib.md5()
md5_hash.update(data.encode())
print(f"MD5 Hash:        {md5_hash.hexdigest()}")

# SHA-1 Hash (160-bit)
sha1_hash = hashlib.sha1()
sha1_hash.update(data.encode())
print(f"SHA-1 Hash:      {sha1_hash.hexdigest()}")

# SHA-224 Hash (224-bit)
sha224_hash = hashlib.sha224()
sha224_hash.update(data.encode())
print(f"SHA-224 Hash:    {sha224_hash.hexdigest()}")

# SHA-256 Hash (256-bit) - Original example
sha256_hash = hashlib.sha256()
sha256_hash.update(data.encode())
print(f"SHA-256 Hash:    {sha256_hash.hexdigest()}")

# SHA-384 Hash (384-bit)
sha384_hash = hashlib.sha384()
sha384_hash.update(data.encode())
print(f"SHA-384 Hash:    {sha384_hash.hexdigest()}")

# SHA-512 Hash (512-bit)
sha512_hash = hashlib.sha512()
sha512_hash.update(data.encode())
print(f"SHA-512 Hash:    {sha512_hash.hexdigest()}")

# BLAKE2b Hash (variable length, default 512-bit)
blake2b_hash = hashlib.blake2b()
blake2b_hash.update(data.encode())
print(f"BLAKE2b Hash:    {blake2b_hash.hexdigest()}")

# BLAKE2s Hash (variable length, default 256-bit)
blake2s_hash = hashlib.blake2s()
blake2s_hash.update(data.encode())
print(f"BLAKE2s Hash:    {blake2s_hash.hexdigest()}")

# SHA-3 family (if available)
try:
    # SHA3-256
    sha3_256_hash = hashlib.sha3_256()
    sha3_256_hash.update(data.encode())
    print(f"SHA3-256 Hash:   {sha3_256_hash.hexdigest()}")
    
    # SHA3-512
    sha3_512_hash = hashlib.sha3_512()
    sha3_512_hash.update(data.encode())
    print(f"SHA3-512 Hash:   {sha3_512_hash.hexdigest()}")
    
    # SHAKE-128 (extendable output function)
    shake_128_hash = hashlib.shake_128()
    shake_128_hash.update(data.encode())
    print(f"SHAKE-128 Hash:  {shake_128_hash.hexdigest(32)}")  # 32 bytes output
    
except AttributeError:
    print("SHA-3 functions not available in this Python version")


print("=" * 50)
print("\nHash Function Comparison:")
print("MD5:      Fast but cryptographically broken - avoid for security")
print("SHA-1:    Deprecated for cryptographic use due to vulnerabilities")
print("SHA-2:    Widely used and secure (SHA-224, SHA-256, SHA-384, SHA-512)")
print("SHA-3:    Latest standard, different design from SHA-2")
print("BLAKE2:   Fast and secure, good alternative to SHA-2")