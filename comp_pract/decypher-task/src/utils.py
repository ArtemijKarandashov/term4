from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def decrypt(raw_key, secret):
    key = RSA.import_key(raw_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    decrypted_message = cipher_rsa.decrypt(secret)
    return decrypted_message.decode('utf-8')

def generate_pair():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    with open("public_key.pem", "wb") as f:
        f.write(public_key)
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    
    return public_key, private_key

def encrypt_message(secret_message: str):
    with open("public_key.pem", "rb") as f:
        recipient_public_key = RSA.import_key(f.read())
    
    with open("private_key.pem", "rb") as f:
        raw_key = f.read()

    cipher_rsa = PKCS1_OAEP.new(recipient_public_key)

    encoded_message = secret_message.encode('utf-8')
    encrypted_message = cipher_rsa.encrypt(encoded_message)

    return raw_key, encrypted_message