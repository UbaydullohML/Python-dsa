class Node:
    def __init__(self, value):  #create a new node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):   #creat a new node & initialize new linked list
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)  # Output: 4

    # def append(self, value):  #add a new node to the end of the linked list
    # def prepend(self, value):  #add a new node to the beginning of the linked list
    # def insert(self, index, value): # create new node, insert node
