# CryptoGraphy

## 1️⃣ **What is Cryptography?**

🔒 **Cryptography** is the science (and art) of securing information so that only intended recipients can read or process it.

- It transforms **plaintext** (readable data) into **ciphertext** (scrambled data) to protect its contents.
- Cryptography helps in ensuring data privacy, authenticity, and integrity.
- It’s used everywhere today: online banking, messaging apps, e-commerce, etc.

Think of cryptography like writing a secret code that only someone with the key can decode.

---

## 2️⃣ **Key Concepts**

Let’s break down the essential terms:

### 🔑 **Plaintext**

- Original readable message or data.
- Example: "HELLO WORLD"

### 🔑 **Ciphertext**

- The encrypted, unreadable version of plaintext.
- Example (Caesar Cipher with shift 3): "KHOOR ZRUOG"

### 🔑 **Encryption**

- The process of converting plaintext into ciphertext using an algorithm and a **key**.
- Example: Using a shift of 3 in Caesar Cipher.

### 🔑 **Decryption**

- The process of converting ciphertext back into plaintext using a **key**.
- Example: Reversing the shift in Caesar Cipher.

### 🔑 **Key**

- A secret value used in encryption and decryption to scramble and unscramble data.
- Without the key, decryption is practically impossible (in good cryptography).

---

## 3️⃣ **Cryptographic Goals**

🔐 Cryptography aims to achieve four major security properties:

### ✅ **Confidentiality**

- Only authorized parties can access the information.
- Example: Encrypting your messages so only the recipient can read them.

### ✅ **Integrity**

- Ensures that data is not altered in transit.
- Example: Digital signatures verify a file hasn’t been tampered with.

### ✅ **Authentication**

- Confirms the identity of the sender or receiver.
- Example: Logging in to your email with a password verifies your identity.

### ✅ **Non-repudiation**

- The sender cannot deny having sent the information.
- Example: Digital signatures can prove someone sent a message.

---

## 4️⃣ **Historical Ciphers (for Fun!)**

Before modern cryptography, simpler ciphers were used:

### 🔄 **Caesar Cipher**

- A substitution cipher that shifts letters by a fixed number.
- Example: Shift by 3.
    - Plaintext: "HELLO"
    - Ciphertext: "KHOOR"
- Easy to break today but was effective in Julius Caesar’s time.

### 🔄 **Vigenère Cipher**

- A more advanced cipher that uses a **keyword** to shift letters.
- Example:
    - Keyword: "KEY"
    - Plaintext: "HELLO"
    - Key repeated: "KEYKE"
    - Each letter is shifted by the alphabetical value of the key’s letters.
- More secure than Caesar but still breakable with modern techniques.

# Key Concepts used in Development

[**Hashing**](https://www.notion.so/Hashing-206a553d37b480cea6c0de8ef1b5067c?pvs=21)

[**Salting**](https://www.notion.so/Salting-206a553d37b4806fada0d2a6481cf417?pvs=21)

[**HMAC**](https://www.notion.so/HMAC-206a553d37b4805da1d6f7b54fd4cbb6?pvs=21)

[**Symmetric Encryption**](https://www.notion.so/Symmetric-Encryption-206a553d37b48045878cf629c4183165?pvs=21)

[**Asymmetric Encryption**](https://www.notion.so/Asymmetric-Encryption-206a553d37b4809b8730c659c45e4d75?pvs=21)

[**Digital Signing** ](https://www.notion.so/Digital-Signing-206a553d37b4807ba38fd1d6d953af88?pvs=21)