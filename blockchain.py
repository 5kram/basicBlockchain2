#Import statements
import hashlib as hasher 
import random as rand
import time 
import datetime as date
#import ipyparallel as ipp
#import numpy as np
#import matplotlib.pyplot as plt

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

"""
# Testing 1
# Passed test
def test_question_1(index, time, data, previous_hash):
    new_block = Block(index, time, data, previous_hash)
    check_string = '2def27922fc1c67254a9cdb0c660b91abf9b135ad38fc13c7c77007448b824a0'
    print_statement = "PASSED!!! Move on to next Question" if str(new_block.hash) == check_string else "FAILED!!! Try Again"
    print(print_statement)
    
time = '2019-10-17 00:37:35.256774'
data = 'Machine Learning Blockchain AI'
previous_hash = '6ffd1464f68ef4aeb385d399244efa19293ba5c842c464a82c02f8256ef71428'
index = 0
    
test_question_1(index, time, data, previous_hash)
"""

#Creates the first block with current time and generic data
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

#Function that creates the next block, given the last block on the chain you want to mine on
def next_block(last_block, nonce=0):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = "Hey! I'm block " + str(index)
    previous_hash = last_block.hash
    return Block(index, timestamp, data, previous_hash, nonce)

"""
# Testing 2
# Passed test
def test_question_2(genesis_block):
    block_1 = next_block(genesis_block)
    if block_1.index == 1 and block_1.data == "Hey! I'm block 1" and block_1.previous_hash == genesis_block.hash and str(type(block_1.timestamp)) == "<class 'datetime.datetime'>":
        print("PASSED!!! Move on to next part" )
    else:
        print("FAILED!!! Try again :(")
    

genesis_block = create_genesis_block()
test_question_2(genesis_block)
"""