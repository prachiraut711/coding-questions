class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#Connecting nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

#Printing the linked list
current = node1
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")



# 1)Traversing in Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")


# 2)Insertion at the begining
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
new_node = Node(50)
new_node.next = head
head = new_node

#function to print
def print_list(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

print_list(head)


# 3)Insertion at the end
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

new_node = Node(50)
head = node1
current = head
while current.next is not None:
    current = current.next
current.next = new_node

#function to print
def print_list(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

print_list(node1)


# 4) Insertion a node at the specific position
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

new_node = Node(25)
current = node1
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

#function to print
def print_list(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

print_list(node1)


# 5) Deletion node from begining
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

if head is not None:
    head = head.next

current = head
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")


# 6) Deletion at end
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

current = head
while current.next.next is not None:
    current =current.next
current.next = None

# Function to print linked list
def print_list(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Print the list
print_list(head)
    

# 7) Deletion at particular node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

current = head
while current.next.data != 30:
    current = current.next
current.next = current.next.next

# Function to print linked list
def print_list(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Print the list
print_list(head)