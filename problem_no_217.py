# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.
# Custom testing:
# For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
# We will build the linked list and pass the node to your function.
# The output will be the entire list after calling your function.
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next    #not return anything BCZ  You're not creating a new list or returning a modified list — you're just mutating the existing list structu


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    
    node_to_delete = head.next  # Node with value 5

    # Correct method call using instance of Solution
    Solution().deleteNode(node_to_delete)

    print(print_list(head))  # Output: [4, 1, 9]


if __name__ == "__main__":
    main()



# 🎯 Goal:
# After deleting 5, the list should become:
# [4, 1, 9]
# ❗ Constraint:
# You can’t go backwards in a singly linked list, so you can't find the node before 5.
# So how can you "remove" this node?
# ✅ Trick (again):
# We can't delete 5 directly, but we can:
# Copy the value of 5.next (which is 1) into the current node:
# node.val = node.next.val  # now node.val = 1
# Skip over the next node:
# node.next = node.next.next  # node.next = node with value 9
# Now the node that originally had 5 becomes:
# [4, 1, 9]
# Even though we never deleted the actual node 5, we replaced its value and skipped over the next node. That's why it looks like 5 is deleted.
# ✅ Final Python Code
# class Solution:
#     def deleteNode(self, node):
#         node.val = node.next.val
#         node.next = node.next.next
# 🔁 Step-by-step Example
# Let's build the original linked list:
# Index:  [0]  [1]  [2]  [3]
# List:   4 →  5 →  1 →  9
#              ↑
#          (node to delete)
# Apply the trick:

# node.val = 1 → The node becomes 1 → 1 → 9

# node.next = 9 → The node becomes 1 → 9

# Now the list looks like:
# 4 → 1 → 9
# And we're done.