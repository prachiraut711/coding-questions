# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.


#O(n) approch
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

def getLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def deleteMid(head):
    length = getLength(head)

    if length == 1:
        return None
    
    middle_index = length // 2

    current = head
    for i in range(middle_index - 1):
        current = current.next
    current.next = current.next.next
    
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    head = deleteMid(head)
    print(print_list(head))

if __name__ == "__main__":
    main()


#O(1) approch
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteMid(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next  #prev comes before sloe this sequence is important

    prev.next = slow.next 

    return head

def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    head = deleteMid(head)
    print(print_list(head))

if __name__ == "__main__":
    main()
    
#for example = 10,20,30,40,50
# prev = slow must come before slow = slow.next
# Step-by-step execution with the correct order:

# fast = fast.next.next   # fast = 30
# prev = slow             # prev = 10
# slow = slow.next        # slow = 20
# Next loop:

# fast = fast.next.next   # fast = 50
# prev = slow             # prev = 20
# slow = slow.next        # slow = 30
# Next loop:

# fast = None (loop ends)
# Now:

# slow is pointing to 30 (middle)
# prev is pointing to 20
# prev.next = slow.next  # 20 → 40
# ✅ Resulting list: 10 → 20 → 40 → 50




#for example = 10,20,30,40,50
# ✅ Step-by-Step with Values
# We start with:
# slow = head  # 10
# fast = head  # 10
# prev = None
# 🌀 Loop Iterations:
# 🟢 1st iteration:
# fast = 10, fast.next = 20 → ✅ loop runs

# Move pointers:

# fast = fast.next.next → 30
# prev = slow           → 10
# slow = slow.next      → 20
# 🟢 2nd iteration:
# fast = 30, fast.next = 40 → ✅ loop runs

# Move pointers:

# fast = fast.next.next → 50
# prev = slow           → 20
# slow = slow.next      → 30
# 🟢 3rd iteration:
# fast = 50, fast.next = 60 → ✅ loop runs

# Move pointers:

# fast = fast.next.next → None
# prev = slow           → 30
# slow = slow.next      → 40
