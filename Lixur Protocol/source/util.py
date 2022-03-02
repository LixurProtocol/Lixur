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



# Code for recycling
'''
    def transfer(self, public_key, private_key, recipient, amount):
        recipient = next(v for k, v in self.network_assets["list"] if str(recipient) in k)
        # If a recipient address doesn't exist, return an error
        # I also need to verify signatures as well
        # Hash signatures and append them to the transaction

        def cryptographic_police(public_key, private_key, recipeint, amount):
            try:
                signature = sphincs_sign(private_key, bytes(f"{public_key} -> {recipient}"), 'utf-8')
                assert signature
                assert verify(public_key, bytes((f"{public_key} -> {recipient}: Amount: {amount}"), 'utf-8'), signature)
                print("[+] Transaction verified.")
            except AssertionError:
                print("[-] Transaction failed, invalid cryptographic signature.")

        if public_key in network_assets["list"].keys():
            if amount >= self.balance[balance]:
                tangle = Tangle()
                tangle.make_transaction()
                cryptographic_police(public_key, private_key, recipient, amount)
                self.addresses[balance] -= amount
                recipient[balance] += amount
                print("[+] Withdraw Successful. Current Balance: (%s)" % str(self.addresses[address]))
                return self.addresses[balance]
            else:
                print("[-] Insufficient Funds")
                return None
        else:
            print("[-] This wallet does not have such an address!! (%s)" % address)
            return None
            
            
    graph = self.graph
        for tip in confirmed_transactions:
            tip_list = []
            tip_list.append(tip)
            for key in graph:
                for tip in tip_list:
                    if key == tip:
                        print(f'Success! {key} = {tip}')
                        weights = []
                        if graph[key].previous_hashes == None or "None":
                            continue
                        elif graph[key].previous_hashes != None or "None":
                            print("nice")
                            weights.append(graph[key].previous_hashes)
                            print(f'weights: {type(weights)}')
                            cumulative_weight = sum(weights)
                            print("[+] Cumulative weight: %d" % cumulative_weight)
                            return cumulative_weight
                            
        

    def is_valid_transaction(self, transaction):
        if transaction.signature == None or len(transaction.signature) != 64:
            print(str({'[!] Invalid signature'}))
            return None
        elif len(transaction.signature) == 64:
            if transaction.previous_hashes == None and transaction.index == 0 or len(transaction.previous_hashes) == 2:
                return True
        '''

'''
        TODO: implement transaction validation logic.

        We first need to make sure necessary things are appended such as a valid signature, and confirmed transactions.

        We then to check if the sending wallet has enough amount if the transaction isn't void. Look through the ledger for this or we can
        use the get_balance() function to instantly determine the balance of a given sending address.

        After transaction validation has been completed, consensus has to be ran. This is where we need to implement the consensus algorithm.

        If anywhere we encounter an error, we cancel and revoke the transaction and say it's invalid and list why.
        If there is no errors, we append the transaction to the ledger.
'''
