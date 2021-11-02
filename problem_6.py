class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1='null', llist_2='null'):
    # test case
    #empty null
    if llist_1=='null' or llist_2=='null':
        return "please insert appropriate input"
    # empty lists
    if llist_1.head==None:
        return llist_2
    if llist_2.head==None:
        return llist_1
    # Your Solution Here
    # 1. I will form set of all the value in both of the list than I'll create the new linked list which contain all
    # the item in the set( I'm using set in order to prevent repetition)
    set_items=set()
    set_items.add(llist_1.head.value)
    node=llist_1.head
    while node.next:
        node=node.next
        set_items.add(node.value)
    set_items.add(llist_2.head.value)
    node=llist_2.head
    while node.next:
        node=node.next
        set_items.add(node.value)
    ## 2. create linklist of all the item in the set
    llist_union=LinkedList()
    for item in set_items:
        llist_union.append(item)
    return llist_union


def intersection(llist_1='null', llist_2='null'):
    ## test case
    # epmty input
    if llist_1=='null' or llist_2=='null':
        return "please insert appropriate input"
    # empty list
    if llist_1.head == None:
        return LinkedList()
    if llist_2.head == None:
        return LinkedList()
    #1. check llist1 and add the node value as key to dictionarry with value 0
    dict_node=dict()
    dict_node[(llist_1.head.value)]=0
    node = llist_1.head
    while node.next:
        node = node.next
        dict_node[node.value]=0
    # 2. check llist2, if the node.value exist in the dic , the value is 1
    if llist_2.head.value in dict_node:
        dict_node[llist_2.head.value]=1
    node=llist_2.head
    while node.next:
        node=node.next
        if node.value in dict_node:
            dict_node[node.value]=1
    # 3. create new linked list of the intersection -- only fore key with value 1, mean it show both of the linked list
    llist_intersection=LinkedList()
    for key in dict_node:
        if dict_node[key]==1:
            llist_intersection.append(key)

    return llist_intersection


# Test case 1- regular case

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#return 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
#return 4 -> 6 -> 21 ->

# Test case 2 - regular case - without union

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
#return
#return 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->


# Test case 3 - empty list
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
#return
#return 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->

# Test case 4 - empty  2 list
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_1 = []
element_2 = []
for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_5,linked_list_7))
print (intersection(linked_list_5,linked_list_8))
#return
#return

# Test case 4 - empty  input
print (union())
print (intersection())
#return- please insert appropriate input
#return- please insert appropriate input
