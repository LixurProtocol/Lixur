# Lixur uses the "Falcon 1024" post-quantum, lattice-based cryptography.
# Sign function signs the private keys, usage -> sign(private_key, message)
# Verify function verifies the signature, usage -> verify(public_key, message, signature)
# Generate keypair function generates the public and private keys, usage -> generate_keypair()
from pqcrypto.sign.falcon_1024 import verify, generate_keypair, sign
from hashlib import sha256
from util import Util as util
import binascii
import random
import os
import hashlib
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

util = util()

class KeyGen:
    def __init__(self):
        self.public_key, self.private_key = generate_keypair()  # Keys are in bytes.
        self.address = KeyGen.generate_addresses(self)
        self.available_addresses = []

    @staticmethod
    def generate_addresses(self):
        self.alphanumeric_address = hashlib.sha256(self.public_key).hexdigest()
        return self.alphanumeric_address

    @staticmethod
    def get_alphanumeric_address(self):
        return self.alphanumeric_address

    @staticmethod
    def get_readable_address(self):
        name = input("[+] Enter a permanent readable address for Lixur (Type '`' to cancel): ")
        if name == "`":
            print("[-] Readable Address Generation Cancelled!")
            self.readable_address = None
        else:
            while name in self.available_addresses:
                print("[!] This address is already in use! Please try again.")
                name = input("[+] Enter a permanent readable address for Lixur (Type '`' to cancel): ")
            else:
                self.readable_address = name.lower().replace(' ', '_') + ".lxr"
                self.available_addresses.append(self.readable_address)
        return self.readable_address

    @staticmethod
    def sign_tx(public_key, private_key, message):
        signature = sign(private_key, message.encode('utf-8'))
        try:
            x = verify(public_key, message.encode('utf-8'), signature)
            assert x
            hashed_signature = sha256(signature).hexdigest()
        except AssertionError:
            print("[!] Signature verification failed. Invalid or non-existent signature")
        return hashed_signature

    @staticmethod
    def get_public_key(self):
        return self.public_key

    @staticmethod
    def get_private_key(self):
        return self.private_key

    @staticmethod
    def generate_decryption_phrase(self):
        try:
            with open("source/decrypt_words.txt", "r", encoding="utf-8") as f:
                words = f.readlines()
        except FileNotFoundError:
            with open("decrypt_words.txt", "r", encoding="utf-8") as f:
                words = f.readlines()
        word_list = []
        number = 8  # Only 4, 6 or 8 are acceptable and the higher, the more secure.
        for i in range(number):
            index = random.randint(1, 2500)
            word_list.append(words[index].strip())
        # turn the list into a string
        word_list = " ".join(word_list)
        f.close()
        return word_list

    @staticmethod
    def login_lixur(self):
        new_wallet = input('Welcome to Lixur! Input "new" to create a new wallet, or "existing" to access an existing one: ')
        new_wallet = new_wallet.lower()

        if new_wallet == "new":
            self.is_new_wallet = True
        elif new_wallet == "existing":
            try:
                file = open("lixur_keystore.txt", "x")
                file.close()
                print("[!] No existing wallet found. Creating a new wallet...")
                self.is_new_wallet = True
            except FileExistsError:
                self.is_new_wallet = False
        return self.is_new_wallet

    @staticmethod
    def wallet(self):
        if self.login_lixur(self) == True:
            self.phrase = self.generate_decryption_phrase(self)
            self.input_encrypt = {
                "_": self.get_private_key(self),
                "__": self.get_public_key(self),
                "___": self.get_readable_address(self),
            }
            self.encrypt = bytes(str(self.input_encrypt), 'utf-8')
            util.aes_wallet_encrypt(self.encrypt, self.phrase)
        elif self.is_new_wallet == False:
            result = util.aes_wallet_decrypt(self.get_keystore(self)[1], self.get_keystore(self)[0])
            self.private_key = result[0]
            self.public_key = result[1]
            self.alphanumeric_address = result[2]
            self.readable_address = result[3]

    @staticmethod
    def get_ex_private_key(self):
        if self.private_key is None:
            print("[!] No existing wallet found. Creating a new wallet...")
            self.wallet()
            return self.private_key
        elif self.private_key is not None:
            return self.private_key

    @staticmethod
    def get_ex_public_key(self):
        if self.public_key is None:
            print("[!] No existing wallet found. Creating a new wallet...")
            self.wallet()
            return self.public_key
        elif self.private_key is not None:
            return self.public_key

    @staticmethod
    def get_ex_alphanumeric_address(self):
        if self.alphanumeric_address is None:
            print("[!] No existing wallet found. Creating a new wallet...")
            self.wallet()
            return self.alphanumeric_address
        elif self.alphanumeric_address is not None:
            return self.alphanumeric_address

    @staticmethod
    def get_ex_readable_address(self):
        if self.readable_address is None:
            print("[!] No existing wallet found. Creating a new wallet...")
            self.wallet()
            return self.readable_address
        elif self.readable_address is not None:
            return self.readable_address

    @staticmethod
    def get_keystore(self):
        try:
            with open ("lixur_keystore.txt", "r", encoding="utf-8") as f:
                keystore_dict = eval(f.read())
                hash = keystore_dict['hash']
            return keystore_dict, hash
        except FileNotFoundError:
            with open("lixur_keystore.txt", "r", encoding = "utf-8'") as f:
                keystore_dict = eval(f.read())
                hash = keystore_dict['hash']
            return keystore_dict, hash
