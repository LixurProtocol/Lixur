import hashlib
from uuid import uuid4
import json

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
            print("Keystore not found.")
    def get_phrase(self):
        try:
            with open("source/phrase.txt", "r") as f:
                user_input = f.read().replace(" ", "")
                return user_input
        except FileNotFoundError:
            print("Phrase not found.")
    def get_graph(self):
        try:
            filename = "database/graph.json"
            with open(filename, 'r') as f:
                graph_data = dict(json.load(f))
            return graph_data
        except FileNotFoundError:
            print("Graph not found.")
    def get_graph_tx_count(self):
        try:
            graph_data = self.get_graph()
            return len(graph_data.keys())
        except FileNotFoundError:
            print("Graph not found.")
    def get_balance(self, address):
        balance = 0
        appearances = 0
        graph_data = self.get_graph()
        for tx in graph_data:
            if address == graph_data[tx]['sender'] or address == graph_data[tx]['recipient']:
                appearances += 1
            if address == graph_data[tx]['sender'] and graph_data[tx]['recipient'] and appearances == 1 or 2:
                if address in graph_data[tx]['sender']:
                    balance -= int(graph_data[tx]["amount"])
                if address == graph_data[tx]["recipient"]:
                    balance += int(graph_data[tx]["amount"] * 2)
            else:
                for tx in graph_data:
                    if address in graph_data[tx]['sender']:
                        balance -= int(graph_data[tx]["amount"])
                    if address == graph_data[tx]["recipient"]:
                        balance += int(graph_data[tx]["amount"])
        return balance
