# Blockchain in Python
import hashlib as hasher 
import random as rand
import time 
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        """ __init__ function that creates a new block given some parameters. """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.hash_block()

    def hash_block(self):
        """ hash_block function that computes the hash of this block based on its class variables. """
        message = str(self.index) + str(self.timestamp) + self.data + self.previous_hash + str(self.nonce)
        hash = hasher.sha256()
        hash.update(message.encode('utf-8'))
        return hash.hexdigest()

# Creates the first block with current time and generic data
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Function that creates the next block, given the last block on the chain you want to mine on
def next_block(last_block, nonce=0):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = "Hey! I'm block " + str(index)
    previous_hash = last_block.hash
    return Block(index, timestamp, data, previous_hash, nonce)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain[0]

# How many blocks should we add to the chain after the genesis block
num_blocks = 20

def complete_chain(num_blocks, blockchain, previous_block):
    # Add blocks to the chain
    for i in range(0, num_blocks):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))

complete_chain(num_blocks, blockchain, previous_block)

def generate_nonce(length=20):
    return ''.join([str(rand.randint(0, 9)) for i in range(length)])

def generate_difficulty_bound(difficulty=1):
    diff_str = ""
    for i in range(difficulty):
        diff_str += '0'
    for i in range(64 - difficulty):
        diff_str += 'F'
    diff_str = "0x" + diff_str  # "0x" needs to be added at the front to specify that it is a hex representation
    return(int(diff_str, 16))  # Specifies that we want to create an integer of base 16 (as opposed to the default base 10)

# Given a previous block and a difficulty metric, finds a nonce that results in a lower hash value
def find_next_block(last_block, difficulty, nonce_length):
    difficulty_bound = generate_difficulty_bound(difficulty)
    start = time.process_time() 
    new_block = next_block(last_block)
    hashes_tried = 1

    while True:
        hex_hash = "0x" + new_block.hash
        hex_hash = int(hex_hash, 16)
        if hex_hash < difficulty_bound:
            break
        nonce = generate_nonce
        new_block = next_block(last_block, nonce)
        hashes_tried = hashes_tried + 1


    time_taken = time.process_time() - start
    return(time_taken, hashes_tried, new_block)

# Create the blockchain and add the genesis block
blockchain_pow = [create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain_pow[0]

# How many blocks should we add to the chain after genesis block
num_blocks = 20

# magnitude of difficulty of hash - number of zeroes that must be in the beginning of the hash
difficulty = 3

# length of nonce that will be generated and added
nonce_length = 20

# Add blocks to the chain based on difficulty with nonces of length nonce_length
def create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length, print_data=1):
    hash_array = []
    time_array = []
    for i in range(0, num_blocks):
        time_taken, hashes_tried, block_to_add = find_next_block(previous_block, difficulty, nonce_length)
        blockchain_pow.append(block_to_add)
        previous_block = block_to_add
        hash_array.append(hashes_tried)
        time_array.append(time_taken)
        # Tell everyone about it!
        if print_data:
            print("Block #{} has been added to the blockchain!".format(block_to_add.index))
            print("{} Hashes Tried!".format(hashes_tried))
            print("Time taken to find block: {}".format(time_taken))
            print("Hash: {}\n".format(block_to_add.hash))
    return(hash_array, time_array)

hash_array, time_array = create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length)
