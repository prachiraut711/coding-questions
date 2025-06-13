# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
# Given a list like:
# Index from front:   1 → 2 → 3 → 4 → 5  
# Index from end:     5 ← 4 ← 3 ← 2 ← 1
# So:
# If n = 2, you remove 4 (the 2nd node from the end).
# If n = 1, you remove 5 (the last node).
# If n = 5, you remove 1 (the first node).


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head    #this is dummy head node withvalue 0
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    
    return dummy.next


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

    head = removeNthFromEnd(head, 2)
    print(print_list(head))

if __name__ == "__main__":
    main()

    

# ✅ Step-by-Step Dry Run
# 📌 1. Initial Setup
# We first create a dummy node that points to the head:
# dummy → 1 → 2 → 3 → 4 → 5
# We also initialize two pointers:
# Edit
# first = dummy
# second = dummy
# So both pointers are currently at the dummy node.
# 📌 2. Move first pointer n + 1 = 3 steps ahead
# 1st step:
# first = first.next  # first → 1
# 2nd step:
# first = first.next  # first → 2
# 3rd step:
# first = first.next  # first → 3
# Now the pointers look like this:

# dummy → 1 → 2 → 3 → 4 → 5
#           ↑         ↑
#        second     first
# There is a gap of 2 nodes between first and second.

# 📌 3. Move both first and second until first reaches the end
# 1st iteration:

# first = first.next      # first → 4
# second = second.next    # second → 1
# 2nd iteration:

# first = first.next      # first → 5
# second = second.next    # second → 2
# 3rd iteration:

# first = first.next      # first → None (end of list)
# second = second.next    # second → 3
# Now the pointers look like this:


# dummy → 1 → 2 → 3 → 4 → 5
#                     ↑
#                  second
# 📌 4. Delete the node after second (which is node 4)

# second.next = second.next.next
# This skips node 4 and links node 3 directly to node 5.

# Now the list becomes:

# dummy → 1 → 2 → 3 → 5
# 📌 5. Return the new head

# return dummy.next
# This skips the dummy node and returns the updated list:


# [1, 2, 3, 5]
# ✅ Final Output:
# python
# Copy
# Edit
# [1, 2, 3, 5]
# Node with value 4 (2nd from end) is successfully removed!


# The underscore _ is a throwaway variable.

# It means: “I don’t care about this value.”

# In this loop, you're only interested in doing something n + 1 times — you don’t need the actual loop variable.

# Variable	Contains	Good to Return?
# second.next	Node being deleted or after it	❌ No
# dummy.next	Updated head of the list	✅ Yes


# method 2 without dummy but you have to add edge case if we have to delete head here
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    # Edge case: if fast is None, we are deleting the head
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

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

    head = removeNthFromEnd(head, 3)
    print(print_list(head))

if __name__ == "__main__":
    main()