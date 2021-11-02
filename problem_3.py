import sys
class Internal_Node:
    def __init__(self,value):
        self.freq=value
        self.right=None
        self.left=None

class Node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.right=None
        self.left=None

class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i].freq < self.heap_list[i // 2].freq:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2

    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)

    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i].freq > self.heap_list[mc].freq:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i * 2].freq < self.heap_list[(i * 2) + 1].freq:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'

        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]

        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]

        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list

        # Decrease the size of the heap
        self.current_size -= 1

        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)

        # Return the min value of the heap
        return root

    def size(self):
        return len(self.heap_list)
    pass

def freq_table(data):
    ## helper function-- get string and return dict of freq table
    freq_table=dict()
    data= list(data)
    for i in data:
        if i in freq_table:
            freq_table[i]+=1
        else:
            freq_table[i]=1
    return freq_table

def form_min_heap(freq_dic):
    ## Helper function- get freq table and return MinHeap of nodes
    min_heap_nodes=MinHeap()
    for key in freq_dic:
        min_heap_nodes.insert(Node(key,freq_dic[key]))
    return min_heap_nodes

def encoding(data,endcod_dic):
    ## Helper function- get data and code dictionary and return the encoded data
    code=''
    for let in list(data):
        code+=endcod_dic[let]
    return code

def huffman_encoding(data):
    # pre case-- if there is one letter or no letter
    if len(list(data))==1:
        return 1,Node(char=data,freq=1)
    if len(list(data))==0:
        return 0,None

    #1.Create frequency table( by dictionary)
    freq_dic=freq_table(data)
    if freq_dic.__len__()==1:
        return 1, Node(char=data, freq=1)
    #2. create min heap of nodes
    min_heap_nodes=form_min_heap(freq_dic)
    ## 3.a- main function- initiate the hoffman structure  creating 2 nodes and internal node
    node1=min_heap_nodes.delete_min()
    node2=min_heap_nodes.delete_min()
    first_int_node=Internal_Node(node1.freq+node2.freq)
    first_int_node.left=node1
    first_int_node.right=node2
    min_heap_nodes.insert(first_int_node)
    ##3b.main function- create the hoffman structure repeating process
    """
    the loop run over the min heap and and delete the lowest 2 value and return the internal node( according to the algorithm )
    the loop stops when there is single node in the tree
    """
    while min_heap_nodes.current_size>1:
        node1 = min_heap_nodes.delete_min()
        node2 = min_heap_nodes.delete_min()
        int_node = Internal_Node(node1.freq + node2.freq)
        int_node.left = node1
        int_node.right = node2
        min_heap_nodes.insert(int_node)
    root=min_heap_nodes.delete_min()
    ## 4.Generate the Encoded Data dictionary
    #I'll create local recursive function which call every node in the min heap tree
    # it create dic , the key will be the letter and the value will be the code
    endcod_dic=dict()
    i=''
    def recursive_code(node,i):
        # break case- if i get to final node( not internal node)
        if type(node)==type(Node(1,1)):
            endcod_dic[node.char] = i
            i=0
            return
        # recursive section
        recursive_code(node.right,i+'1')
        recursive_code(node.left,i+'0')
    recursive_code(root,i)
    ## 5.Generate the Encoded Data
    encoded_data=encoding(data,endcod_dic)
    ## return the root of the tree and  the encoded data
    return encoded_data,root


def huffman_decoding(data,tree):
    ## pre case-- if there is one letter or no letter
    if data==1:
        return tree.char
    if data==0:
        return None

    ## 1.Generate the Encoded Data dictionary
    #I'll create local recursive function which call every node in the min heap tree
    # the key will be the code and the value will be the letter
    decoded_dic=dict()
    i=''
    def recursive_code(node,i):
        # break case- if i get to final node( not internal node)
        if type(node)==type(Node(1,1)):
            decoded_dic[i] = node.char
            i=0
            return
        # recursive section
        recursive_code(node.right,i+'1')
        recursive_code(node.left,i+'0')
    recursive_code(tree,i)
    ##2.decode the data
    """
     I'll create loop , the loop  check the first number of the code in 
     in the dic, if it exist it add to the encoded data the value( letter) else, it will check the first two number
     and so on
    """
    decoded_data=''
    data=list(data)
    '''the first loop check every letter-code in entire code'''
    while len(data)!=0:
        check_code=''
        temp_data=data
        '''the sub loop check the combination of the letter-code-- if it exists as a key in the decoded_dic'''
        while check_code not in decoded_dic:
            check_code+=temp_data[0]
            temp_data=temp_data[1:]
        decoded_data+=decoded_dic[check_code]
        data=data[len(check_code):]
    return decoded_data



###TESTS- in the next test the ouput of the huffman_decoding should be equal to value of the insert data
### Test case1- regular sentence
data='Hey my name is Gal and I would like to meet you'
encoded_data,tree=huffman_encoding(data)
decode_data=huffman_decoding(encoded_data,tree)
if decode_data==data:
    print(True)
if decode_data!=data:
    print(False)
## expected output- True

### Test case2- one kind letter sentence
data='hhhhh'
encoded_data,tree=huffman_encoding(data)
decode_data=huffman_decoding(encoded_data,tree)
if decode_data==data:
    print(True)
if decode_data!=data:
    print(False)
## expected output- True

### Test case3-single letter
data='h'
encoded_data,tree=huffman_encoding(data)
decode_data=huffman_decoding(encoded_data,tree)
if decode_data==data:
    print(True)
if decode_data!=data:
    print(False)
## expected output- True

### Test case4-None
data=''
encoded_data,tree=huffman_encoding(data)
decode_data=huffman_decoding(encoded_data,tree)
if decode_data==None:
    print(True)
if decode_data!=None:
    print(False)
## expected output- True