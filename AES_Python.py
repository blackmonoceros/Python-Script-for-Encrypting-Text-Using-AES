from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext
def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)  # Create AES cipher in CBC mode
    iv = cipher.iv  # Initialization vector (IV)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Encrypt with padding
    return iv, ciphertext

# Function to decrypt ciphertext
def decrypt_aes(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES cipher for decryption
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and remove padding
    return plaintext.decode()

# Generate a random encryption key (16 bytes for AES-128)
key = get_random_bytes(16)

# Text to encrypt
plaintext = "This is a secret message!"

# Encrypt the plaintext
iv, ciphertext = encrypt_aes(key, plaintext)
print("Encrypted text:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_aes(key, iv, ciphertext)
print("Decrypted text:", decrypted_text)