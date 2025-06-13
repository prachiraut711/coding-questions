# Given a singly linked list, the task is to find the middle of the linked list. If the number of nodes are even, then there would be two middle nodes, so return the second middle node.
# Example:
# Input: linked list: 1->2->3->4->5
# Output: 3 
# Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.
# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
# Output: 40
# Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.


#This is O(n) approch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head,):
    length = 0
    while head:
        length += 1
        head = head.next

    return length

def getMiddle(head):
    length = getLength(head)
    mid_index = length // 2
    while mid_index:
        head = head.next
        mid_index -= 1

    return head.data

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    print(getMiddle(head))
   
if __name__ == "__main__":
    main()


#the O(1) approch using slow and fast (tortouise method)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))

if __name__ == "__main__":
    main()

# Idea (Fast and Slow Pointers):
# Create two pointers:

# slow: moves one node at a time

# fast: moves two nodes at a time

# When fast reaches the end of the list:

# slow will be at the middle node.
# Loop continues as long as fast and fast.next are not None.

# slow = slow.next: move one step

# fast = fast.next.next: move two steps

# Let’s simulate:

# Step	slow	fast
# Init	10	    10
# 1	    20	    30
# 2	    30	    50
# 3	    40	    None (fast goes past 60)

# Loop ends when fast becomes None.

# So slow is now pointing to 40 → second middle node ✅


#LEETCODE QUESTION
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]: # type: ignore
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Helper function to print list from a given node
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Create object of Solution
    sol = Solution()

    # Get middle node
    middle = sol.middleNode(head)

    # Print the list starting from middle node
    print("Middle node and onwards:")
    printList(middle)
