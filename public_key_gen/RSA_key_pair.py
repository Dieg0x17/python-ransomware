from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(4096)
encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8,
                              )#protection="scryptAndAES128-CBC"

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)

print key.publickey().exportKey()
