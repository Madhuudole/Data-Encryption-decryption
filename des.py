from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = des.encrypt(padded_text.encode())
    return ciphertext

def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    plaintext = des.decrypt(ciphertext).decode().rstrip()
    return plaintext

if __name__ == "__main__":
    key = get_random_bytes(8)
    message = "HelloWorld"
    cipher = des_encrypt(message, key)
    print("Encrypted:", cipher)
    plain = des_decrypt(cipher, key)
    print("Decrypted:", plain)
