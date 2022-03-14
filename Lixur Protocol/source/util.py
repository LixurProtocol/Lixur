import hashlib
from uuid import uuid4
import sys
import json
from base64 import b64decode

class Util:
    def __init__(self, *args):
        pass
    def hash(self, str_input):
        return hashlib.sha256(str_input.encode()).hexdigest()
    def unique_gen(self):
        return str(uuid4()).replace('-', '')
    def str_join(self, *args):
        return ''.join(map(str, args))
    def get_keystore(self):
        try:
            with open("source/lixur_keystore.txt", "r") as f:
                keystore_dict = eval(f.read())
                ks_cipher = b64decode(keystore_dict['cipher_text'].encode('utf-8'))
                ks_nonce = b64decode(keystore_dict['nonce'].encode('utf-8'))
                ks_tag = b64decode(keystore_dict['tag'].encode('utf-8'))
                ks_hash = keystore_dict['hash']
                return ks_cipher, ks_nonce, ks_tag, ks_hash
        except FileNotFoundError:
            raise FileNotFoundError("Keystore not found")
    def get_phrase(self):
        try:
            with open("source/phrase.txt", "r") as f:
                user_input = f.read().replace(" ", "")
                return user_input
        except FileNotFoundError:
            raise FileNotFoundError("Phrase not found.")
    def get_graph(self):
        try:
            filename = "database/graph.json"
            with open(filename, 'r') as f:
                graph_data = dict(json.load(f))
            return graph_data
        except FileNotFoundError:
            raise FileNotFoundError("Graph not found.")
    def get_graph_tx_count(self):
        try:
            graph_data = self.get_graph()
            return len(graph_data.keys())
        except TypeError:
            graph_data = self.get_graph(self)
            return len(graph_data.keys())
        except FileNotFoundError:
            raise FileNotFoundError("Graph not found.")
    def get_appearances(self, address):
        appearances = 0
        graph_data = self.get_graph()
        for tx in graph_data:
            if address == graph_data[tx]['sender'] or address == graph_data[tx]['recipient']:
                appearances += 1
        return appearances
    def get_balance(self, address):
        balance = 0
        graph_data = self.get_graph()
        for tx in graph_data:
            if graph_data[tx]['sender'] == address and graph_data[tx]['recipient'] == address:
                balance += float(graph_data[tx]['amount'])
            if address == graph_data[tx]['sender']:
                balance -= float(graph_data[tx]["amount"])
            if address == graph_data[tx]["recipient"]:
                balance += float(graph_data[tx]["amount"])
        balance = float(balance)
        return balance
