from Crypto.PublicKey import RSA

secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.importKey(encoded_key, passphrase=secret_code)

print key.publickey().exportKey()
