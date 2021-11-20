import blockchain as BC

# Testing 1
def test_1(index, time, data, previous_hash):
    new_block = BC.Block(index, time, data, previous_hash)
    check_string = '2def27922fc1c67254a9cdb0c660b91abf9b135ad38fc13c7c77007448b824a0'
    print_statement = "1 PASSED!!!" if str(new_block.hash) == check_string else "FAILED!!!"
    print(print_statement)
    
time = '2019-10-17 00:37:35.256774'
data = 'Machine Learning Blockchain AI'
previous_hash = '6ffd1464f68ef4aeb385d399244efa19293ba5c842c464a82c02f8256ef71428'
index = 0
    
test_1(index, time, data, previous_hash)

# Testing 2
def test_2(genesis_block):
    block_1 = BC.next_block(genesis_block)
    if block_1.index == 1 and block_1.data == "Hey! I'm block 1" and block_1.previous_hash == genesis_block.hash and str(type(block_1.timestamp)) == "<class 'datetime.datetime'>":
        print("2 PASSED!!!" )
    else:
        print("FAILED!!!")
    

genesis_block = BC.create_genesis_block()
test_2(genesis_block)

# Testing 3
def test_3(blockchain, num_blocks):
    correct = True
    if len(blockchain) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain)-1):
        if blockchain[i + 1].previous_hash != blockchain[i].hash:
            correct = False
            break
    print_statement = "3 PASSED!!!" if correct else "FAILED!!!"
    print(print_statement)

test_3(BC.blockchain, BC.num_blocks)

# Testing 4
def test_4(blockchain_pow, num_blocks):
    correct = True
    bound = BC.generate_difficulty_bound(BC.difficulty)
    if len(blockchain_pow) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain_pow) - 1):
        if blockchain_pow[i + 1].previous_hash != blockchain_pow[i].hash:
            correct = False
            break
        if int(blockchain_pow[i + 1].hash, 16) > bound:
            correct = False
            break
    print_statement = "4 PASSED!!!" if correct else "FAILED!!!"
    print(print_statement)
            
test_4(BC.blockchain_pow, BC.num_blocks)
