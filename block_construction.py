import json
import hashlib

# set constants
TARGET = "0x0000ffff00000000000000000000000000000000000000000000000000000000"
CURRENT_HEIGHT = 836840 # heigth of last block
MINER_ADRESS = "1G1RbsnSQ5hof4KTKk9eeh8jXrjNTtxngU" # base58check
BLOCK_SUBSIDY = 6.25 # current subsidy
MAX_BLOCK_SIZE = 4e6 # weight units

# TODO: check and adapt
def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

class Transaction:
    def __init__(self, version, locktime, vin, vout) -> None:
        self.version = version
        self.locktime = locktime
        self.vin = vin
        self.vout = vout
        self.fee_rate = 0
        self.size = 0

    def is_valid(self) -> bool:
        # amount, signature, block height, double spent, ...
        False
    
    def get_fee_rate(self) -> float:
        return self.fee_rate
    
    def get_size(self) -> int:
        return self.size

class MemPool:
    def __init__(self) -> None:
        self.transactions = []

    def load_file(file) -> Transaction:
        return Transaction()

    def load_mempool(self, dir) -> None:
        for file in dir:
            transaction = self.load_file(file)
            if transaction.is_valid():
                self.add_transaction(transaction)

    def add_transaction(self, transaction) -> None:
        self.transactions.append(transaction)

    def sort_transactions(self) -> None:
        pass

class BlockHeader:
    def __init__(self, version, prev_block_hash, merkle_root, timestamp, difficulty_target, nonce, hash) -> None:
        # bits?
        self.merkle_root = merkle_root
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.timestamp = timestamp
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.hash = hash

class Block:
    def __init__(self) -> None:
        self.header = None # TODO: how to init block header?
        self.transactions = {}
        self.size = 0
    
    def construct_block(self) -> None:
        # TODO: add coinbase
        while self.get_size() <= MAX_BLOCK_SIZE:
            pass

    def add_transaction(self, txid, transaction) -> None:
            self.transactions[txid] = transaction
            self.size += transaction.get_size

    def get_merkle_root(self) -> str:
        return ""
    
    def update_size(self) -> None:
        self

    def get_size(self) -> int:
        return self.size

    def print_block(self) -> None:
        pass