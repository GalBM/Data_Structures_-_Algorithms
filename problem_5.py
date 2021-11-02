import  hashlib
from datetime import datetime

# step1 - define and modify the linked list for contain blocks
class Node:
    def __init__(self, block):
        self.block = block
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
# insert block to the linked list
    def insert(self,block):
        if self.head==None:
            self.head=Node(block)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(block)
#get the last block int the list
    def last_block(self):
        if self.head==None:
            return None
        else:
            node=self.head
            while node.next:
                node=node.next
            return node

## define block, with the clac_hash function as described in the task-- calculate the data, timestamp and the previous hash
class Block:
    def __init__(self, timestamp, data, previous_hash='0'):
      self.timestamp = str(timestamp)
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.timestamp+ self.data+ self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

## Define the object that contain the block each block has node which give the blockchain data structure of linked list
class Blockchain:
    def __init__(self):
        self.llist_block=LinkedList()
        self.num=0
## that function get data and  insert a new block to the exist block chain with the data, current datastamp has and previous hash
    def insert(self,data):
        if self.num==0:
            block= Block(datetime.now(),data)
            self.llist_block.insert(block)
            self.num=1
        else:
            block=Block(datetime.now(),data,previous_hash=self.llist_block.last_block().block.hash)
            self.llist_block.insert(block)
            self.num+=1

## test function- comparing the block has and the afterward block previous hash
def test_check(Block_chain):
    flag=0
    node=Block_chain.llist_block.head
    while node.next:
        if node.block.hash!=node.next.block.previous_hash:
            flag = 1
        node=node.next
    if flag == 0:
        return  print("Work")
    else:
        return print('Error')

## test1 - regular case
MyBlockChain=Blockchain()
MyBlockChain.insert("100")
MyBlockChain.insert("-50")
MyBlockChain.insert("300")
MyBlockChain.insert("750")
MyBlockChain.insert("450")
test_check(MyBlockChain) ## ouput- 'work


## test2 - string numbers and null data
MyBlockChain=Blockchain()
MyBlockChain.insert("100")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("")
MyBlockChain.insert("")
test_check(MyBlockChain)  ## ouput- 'work

## test3 - large amount of blocks
MyBlockChain=Blockchain()
MyBlockChain.insert("100")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("100")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("CAT")
MyBlockChain.insert("COW")
MyBlockChain.insert("100")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
MyBlockChain.insert("-50")
MyBlockChain.insert("dsadsa d")
MyBlockChain.insert("HELLO")
MyBlockChain.insert("DOG")
test_check(MyBlockChain)  ## ouput- 'work
