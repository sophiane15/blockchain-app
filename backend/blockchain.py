import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = str(datetime.now())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "timestamp": self.timestamp
        }, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 4  # Nombre de zéros requis pour le hash

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        })

    def mine_pending_transactions(self):
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.chain[-1].hash
        )
        
        # Proof of Work
        while not new_block.hash.startswith('0' * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)
        self.pending_transactions = []
        print(f"Bloc #{new_block.index} miné ! Hash: {new_block.hash[:10]}...")
