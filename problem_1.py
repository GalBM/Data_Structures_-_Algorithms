class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.main_dic=dict() ## the dict contain the key and value of the inputs
        self.order_dic=dict() ## the dict contain the key , the value is the count of the key exit in the queue
        self.num_of_cap=0 ## the number of the items in the cache
        self.queue=Queue()## Im using queue as the data structure
        self.capacity=capacity
        pass

    def get(self, key="Null"):
        # While the key in the dictionary- it enqueue node and return the value of the key
        # more over, the order_dic increase his size by 1 ( it means we have number of item with the same key in the queue)
        if key=='Null':
            return "please insert key"
        if key in self.main_dic:
            self.queue.enqueue(key)
            self.order_dic[key]=self.order_dic[key]+1
            return self.main_dic[key]
        # the key isnt in the dictionary
        else:
            return -1

    def set(self, key='Null', value='Null'):
        #test case for null input
        if key=="Null" or value=="Null":
            return print("please insert appropriate key and value")
        # there are 2 dict , the main_dic contaion the key and the value , and it add or delete it by the algorithm
        # if there are less than 5 items in the cahce- both the dict get the new key and value
        # and the queue get item
        if self.num_of_cap<self.capacity:
            self.main_dic[key]=value
            self.order_dic[key] = 0
            self.queue.enqueue(key)
            self.num_of_cap+=1
            return
        # when there are more than 5 :
        #1. the queue start droping item- every item it drops, the order_dic reduce 1 untill it get to 0
        #2. when it reach to zero- both of the dic pop the key
        #3. finnaly both of the key add the new key
        else:
            flag=0
            while flag==0:
                key_reduce=self.queue.dequeue()
                if self.order_dic[key_reduce]==0:
                    self.order_dic.pop(key_reduce)
                    self.main_dic.pop(key_reduce)
                    flag=1
                else:
                    self.order_dic[key_reduce]=self.order_dic[key_reduce]-1
            self.main_dic[key] = value
            self.order_dic[key] = 0
        return



#test1 - test the input (set) and output(get) of the function
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

# test2 - test the cache functionallity
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.get(3)
# returns -1 because the cache reached it's capacity and 3 was the least recently use

#test3 -empty chache
our_cache = LRU_Cache(5)
print(our_cache.get(1))
# returns -1

#test4 -null input
our_cache = LRU_Cache(5)
print(our_cache.get())
# returns- please insert key
our_cache.set(4,)
# returns- please insert appropriate key and value
