# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # you forgot this line!

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    l1 = list_to_linked_list([1, 2, 4])
    l2 = list_to_linked_list([1, 3, 4])
    
    solution = Solution()
    merged = solution.mergeTwoLists(l1, l2)
    
    print(linked_list_to_list(merged))

if __name__ == "__main__":
    main()




# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# We represent them as linked lists:

# list1: 1 → 2 → 4
# list2: 1 → 3 → 4
# ✅ Code Setup

# dummy = ListNode(0)    # Dummy starting point
# current = dummy        # Pointer to build merged list
# Initially:

# dummy: 0 → None
# current: points to dummy
# 🔁 Iteration 1
# Compare list1.val (1) and list2.val (1)

# Both are equal, so by convention we take list2 first.

# current.next = list2 → attach node with value 1 from list2

# Move list2 to 3

# Move current to current.next

# State:

# dummy → 1
#            ↑
#         current
# list1: 1 → 2 → 4
# list2: 3 → 4
# 🔁 Iteration 2
# Compare list1.val (1) and list2.val (3)

# 1 < 3, take from list1

# current.next = list1

# Move list1 to 2

# Move current to current.next

# State:

# dummy → 1 → 1
#                 ↑
#              current
# list1: 2 → 4
# list2: 3 → 4
# 🔁 Iteration 3
# Compare list1.val (2) and list2.val (3)

# 2 < 3, take from list1

# current.next = list1

# Move list1 to 4

# Move current to current.next

# State:

# dummy → 1 → 1 → 2
#                       ↑
#                    current
# list1: 4
# list2: 3 → 4
# 🔁 Iteration 4
# Compare list1.val (4) and list2.val (3)

# 3 < 4, take from list2

# current.next = list2

# Move list2 to 4

# Move current to current.next

# State:

# dummy → 1 → 1 → 2 → 3
#                             ↑
#                          current
# list1: 4
# list2: 4
# 🔁 Iteration 5
# Compare list1.val (4) and list2.val (4)

# Equal, take from list2 by default

# current.next = list2

# Move list2 to None

# Move current to current.next

# State:

# dummy → 1 → 1 → 2 → 3 → 4
#                                  ↑
#                               current
# list1: 4
# list2: None
# ✅ Remaining Nodes
# python
# Copy
# Edit
# if list1:
#     current.next = list1
# list1 still has one node left: 4

# Attach it directly

# list1 = None

# Final State:

# dummy → 1 → 1 → 2 → 3 → 4 → 4
#                                            ↑
#                                         current
# list1: None
# list2: None
# ✅ Return Statement
# python
# Copy
# Edit
# return dummy.next
# We skip dummy (value 0), and return:

# 1 → 1 → 2 → 3 → 4 → 4
# 🧾 Final Output

# [1, 1, 2, 3, 4, 4]
# Let me know if you'd like a diagram, or want to go through the recursive version too!
# why return dummy next 

# return dummy.next
# 🔍 First, What is dummy?

# dummy = ListNode(0)
# dummy is a temporary starting node (with value 0) that helps build the merged list.

# It does not contain actual data from list1 or list2.

# It’s used to simplify the code by handling edge cases (like empty input lists) easily.

# 🔗 As we build the merged list:
# We attach new nodes to dummy.next, like this:
# dummy → 1 → 1 → 2 → 3 → 4 → 4
# So dummy is just a placeholder, and the real head of the merged list is at dummy.next.

# 🧠 Why Not Return dummy?
# If you return dummy, the list will start with 0 (the dummy value), which we don’t want:

# # Wrong result if we returned dummy
# [0, 1, 1, 2, 3, 4, 4]
# ✅ Correct Return:

# return dummy.next
# This skips the dummy node and gives you:
# 1 → 1 → 2 → 3 → 4 → 4
# Which is exactly what we want.

# 🧾 Summary
# Concept	Meaning
# dummy	Placeholder to start building the list
# dummy.next	Actual head of the merged list
# return dummy.next	Returns the final merged list, skipping dummy node