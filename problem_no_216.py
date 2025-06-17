# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        def copy_list(head):
            if not head:           #this is IMP for test case =[1]
                return None 

            new_head = ListNode(head.val)
            old_node = head.next
            new_node = new_head

            while old_node:
                new_node.next = ListNode(old_node.val)
                old_node = old_node.next
                new_node = new_node.next

            return new_head     
        
        def isEqual(l1, l2):
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next

            return True
        
        copied = copy_list(head)
        reversed_list = reverse_list(copied)  #reverse of copy list

        return isEqual(head, reversed_list)   #compare kel head means original list with reversed_list ithe copied list barobar nahi kel compare because aplyala original barobar karych ahe .ithe copy list banvli so we get reverse list of that copy list


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    
    print(Solution().isPalindrome(head))   #isPalindrome is defined inside your Solution 

if __name__ == "__main__":
    main()



# 🔁 Step-by-step Execution:
# 1. Check if head is None:
# python
# Copy
# Edit
# if not head:
#     return None
# 👉 Since head is not None, it continues.

# 2. Create the first node of the new list:
# python
# Copy
# Edit
# new_head = Node(head.data)  # Node(1)
# New list:

# makefile
# Copy
# Edit
# Copied: 1 → None
# Pointers:

# old_node = head.next → Node(2)

# new_node = new_head → Node(1)

# 3. Loop through original list:
# python
# Copy
# Edit
# while old_node:
# ✅ First loop:
# python
# Copy
# Edit
# new_node.next = Node(old_node.data)  # new_node.next = Node(2)
# new_node = new_node.next             # move to Node(2)
# old_node = old_node.next             # move to Node(3)
# Copied list:

# css
# Copy
# Edit
# 1 → 2 → None
# ✅ Second loop:
# python
# Copy
# Edit
# new_node.next = Node(3)
# new_node = new_node.next             # move to Node(3)
# old_node = old_node.next             # becomes None → loop ends
# Final Copied list:

# Copy
# Edit
# 1 → 2 → 3
# ✅ Return:
# python
# Copy
# Edit
# return new_head
# So, now copied_head points to:

# csharp
# Copy
# Edit
# 1 → 2 → 3 (new list, separate from original)
# 🎯 Final Result:
# Original list:

# Copy
# Edit
# 1 → 2 → 3
# Copied list:

# Copy
# Edit
# 1 → 2 → 3
# Both are separate in memory — changing one won't affect the other.