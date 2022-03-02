import networkx as nx
from source.util import Util
from random import randint
from collections import OrderedDict
import time
from datetime import datetime
import binascii
import hashlib
from uuid import uuid4
from source.cryptography import KeyGen as keygen
cryptography = keygen()

class Keys:
    genesis_keys = cryptography.generate_addresses(keygen())
    genesis_alphanumeric_address = genesis_keys
    genesis_private_key = cryptography.get_private_key(cryptography)
    genesis_public_key = cryptography.get_public_key(cryptography)

global difficulty
difficulty_level = 1
difficulty = round(int(difficulty_level))  # Figure out how to make this user-adjustable and only ask for it once.

class tx:
    def __init__(self, sender_public_key, recipient_public_key, amount, signature, index):
        self.state = 0
        self.own_weight = 1 * difficulty
        self.cumulative_weight = 0 + self.own_weight
        self.previous_hashes = []
        self.timestamp = datetime.now().strftime('%Y-%m-%d, %H:%M:%S.%f EST')
        self.signature = signature
        self.recipient_public_key = recipient_public_key
        self.sender_public_key = sender_public_key
        self.amount = amount
        self.index = index + 1
        self.nonce = Graph.puzzle(Graph, self.previous_hashes, self.signature, self.timestamp)
    def previous(self):
        x = self.__dict__
        x['previous_hashes'] = list(x['previous_hashes'])
        return x
    def hash_data(data):
        data = str(data).encode('utf-8')
        h = hashsourcenew('sha256')
        h.update(data)
        return h.hexdigest()
    def get_hash(self):
        return hash_data(self.get_transaction_dict())
    def get_transaction_dict(self):
        transaction_dict = OrderedDict({
            'sender' : self.sender_public_key,
            'recipient' : self.recipient_public_key,
            'amount': self.amount,
            'timestamp' : self.timestamp,
            'own_weight' : self.own_weight,
            'cumulative_weight' : self.cumulative_weight,
            'edges' : self.previous_hashes,
            'index' : self.index,
            'signature' : self.signature,
            'nonce' : self.nonce
        })
        return transaction_dict

class Graph():
    def __init__(self, *args):
        self.graph = OrderedDict()
        self.state = 0

        keys = Keys()
        genesis_address = keys.genesis_alphanumeric_address
        genesis_private_key = keys.genesis_private_key
        genesis_public_key = keys.genesis_public_key

        gen_tx_one = tx(genesis_address, genesis_address, 0,
                        keygen.sign_tx(genesis_public_key, genesis_private_key, "Genesis Transaction 1"),
                        index=self.count_tx_number())
        self.update_cumulative_weights(gen_tx_one, ["None"])
        gen_tx_key = self.attach_transaction(gen_tx_one, ["None"])

        gen_tx_two = tx(genesis_address, None, 0,
                        keygen.sign_tx(genesis_public_key, genesis_private_key, "Genesis Transaction 2"),
                        index=self.count_tx_number())
        self.update_cumulative_weights(gen_tx_two, [gen_tx_key])
        self.attach_transaction(gen_tx_two, [gen_tx_key])

        gen_tx_three = tx(genesis_address, None, 0,
                          keygen.sign_tx(genesis_public_key, genesis_private_key, "Genesis Transaction 3"),
                          index=self.count_tx_number())
        self.update_cumulative_weights(gen_tx_three, [gen_tx_key])
        self.attach_transaction(gen_tx_three, [gen_tx_key])
    def count_tx_number(self):
        tx_number = 0
        for x in self.graph:
            tx_number += 1
        return tx_number
    def attach_transaction(self, transaction, confirmed_transactions):
        self.pending_transactions = []
        self.failed_transactions = []
        self.pending_transactions.append(transaction)

        if self.is_valid_transaction(transaction):
            utils = Util()
            x = utils.str_join([
                transaction.timestamp,
                transaction.sender_public_key,
                transaction.recipient_public_key,
                transaction.amount,
                transaction.previous_hashes,
            ])
            transaction.key = utils.hash(x)
            self.tx_key = transaction.key

            for tx in confirmed_transactions:
                transaction.previous_hashes.append(tx)

            self.graph.update({transaction.key: transaction})
            self.pending_transactions.remove(transaction)
            self.state += 1
            return self.tx_key

        else:
            self.failed_transactions.append(transaction)
            raise RuntimeError('[!] Invalid transaction. Attachment failed')
            return None
    def get_pending_transactions(self):
        return self.pending_transactions
    def get_failed_transactions(self):
        return self.failed_transactions
    def does_address_exist(self, address):
        graph = self.graph
        for key in graph:
            a = graph[key]
            if a.sender_public_key == address or a.recipient_public_key == address:
                return True
            else:
                return False
                raise LookupError('The address you are trying to send cryptocurrency to does not exist')
    def is_valid_transaction(self, transaction):
        try:
            if transaction.recipient_public_key == None:
                transaction.recipient_public_key = "None"
            elif transaction != None:
                pass
        except AttributeError:
            if transaction['recipient_public_key'] == None:
                if transaction['amount'] == 0:
                    pass
                elif transaction['amount'] > 0:
                    raise LookupError("[!] Invalid transaction. You can not send cryptocurrency to a non-existent address")
                    return False
            elif transaction['recipient_public_key'] != None:
                pass
        try:
            if transaction.amount == None:
                transaction.amount = 0
        except AttributeError:
            if transaction['amount'] == None and transaction['sender_public_key'] != transaction['recipient_public_key']:
                transaction['amount'] = 0
        try:
            if transaction.signature == None or len(transaction.signature) != 64:
                raise RuntimeError('[!] Invalid signature')
                return False
            elif len(transaction.signature) == 64:
                if transaction.previous_hashes == None and transaction.index == 0 or len(transaction.previous_hashes) == 2:
                    return True
        except AttributeError:
            if transaction['signature'] == None or len(transaction['signature']) != 64:
                raise RuntimeError('[!] Invalid signature')
                return None
            elif len(transaction['signature']) == 64:
                if transaction['previous_hashes'] == None and transaction['index'] == 0 or len(transaction['previous_hashes']) == 2:
                    return True

        '''
        TODO: implement transaction validation logic.

        We first need to make sure necessary things are appended such as a valid signature, and confirmed transactions.

        We then to check if the sending wallet has enough amount if the transaction isn't void. Look through the ledger for this or we can
        use the get_balance() function to instantly determine the balance of a given sending address.

        After transaction validation has been completed, consensus has to be ran. This is where we need to implement the consensus algorithm.

        If anywhere we encounter an error, we cancel and revoke the transaction and say it's invalid and list why.
        If there is no errors, we append the transaction to the ledger.
        '''
        return True
    def confirm_transactions(self):
        tip_one, tip_two = self.select_tips()
        self.is_valid_transaction(tip_one)
        self.is_valid_transaction(tip_two)
        return tip_one['key'], tip_two['key']
    def select_tips(self):
        available_transactions = []
        selected_transactions = []

        tip_quantity = 2

        for key in self.graph:
            _transaction = (self.graph[key].__dict__)
            available_transactions.append(_transaction)

        if len(available_transactions) >= 1:
            for i in range(tip_quantity):
                selected_transactions.append(available_transactions[randint(0, len(available_transactions) - 1)])

            if selected_transactions[0] == selected_transactions[1]:
                while selected_transactions[0] == selected_transactions[1]:
                    selected_transactions[1] = available_transactions[randint(0, len(available_transactions) - 1)]
        return selected_transactions[0], selected_transactions[1]
    def valid_proof(self, previous_hashes, signature, timestamp, nonce):
        guess = (str(previous_hashes) + str(signature) + str(timestamp) + str(nonce)).encode('utf-8')
        h = hashlib.new('sha256')
        h.update(guess)
        guess_hash = h.hexdigest()
        return guess_hash[:difficulty] == '0' * difficulty
    def puzzle(self, previous_hashes, signature, timestamp):
        nonce = 0
        while not self.valid_proof(self, previous_hashes, signature, timestamp, nonce):
            nonce = nonce + 1
        return nonce
    def update_cumulative_weights(self, transaction, confirmed_transactions):
        graph = self.graph
        for key in graph:
            if key in confirmed_transactions:
                a = graph[key]
                self_cumulative_weight = transaction.cumulative_weight
                tip_cumulative_weight = a.cumulative_weight
                a.cumulative_weight = self_cumulative_weight + tip_cumulative_weight
    def make_transaction(self, sender_public_key, recipient_public_key, amount, signature):
        confirmed_transactions = self.confirm_transactions()
        if len(confirmed_transactions) >= 2:
            util = Util()
            if sender_public_key == recipient_public_key:
                if util.get_appearances(sender_public_key) > 0:
                    raise RuntimeError('[!] You cannot send to yourself, what the heck are you doing?')
                else:
                    new_transaction = tx(sender_public_key, recipient_public_key, amount, signature, index=self.count_tx_number())
                    self.update_cumulative_weights(new_transaction, confirmed_transactions)
                    return self.attach_transaction(new_transaction, confirmed_transactions)
            elif sender_public_key != recipient_public_key:
                if self.does_address_exist(recipient_public_key) == True:
                    balance = util.get_balance(sender_public_key)
                    if balance < amount:
                        raise ValueError('You do not have enough funds.')
                    elif balance >= amount:
                        new_transaction = tx(sender_public_key, recipient_public_key, amount, signature, index=self.count_tx_number())
                        self.update_cumulative_weights(new_transaction, confirmed_transactions)
                        return self.attach_transaction(new_transaction, confirmed_transactions)
                elif self.does_address_exist(recipient_public_key) == False:
                    raise LookupError("[!] Recipient address does not exist, please refresh the page and try again.")
        return {'[-] Transaction Failed...'}