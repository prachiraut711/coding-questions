# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next = curr.next    # store next node
        curr.next = prev     # reverse the link
        prev = curr          # move prev forward
        curr = next         # move curr forward
    
    return prev         # prev becomes the new head
 
def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next= Node(5)

    head = reverseList(head)
    print(print_list(head))

if __name__ == "__main__":
    main()


# 🔁 Dry Run: Input = [1,2,3,4,5]
# Step	curr.val	next_node	prev list	Linked List so far
# 1	1	2	1 → None	head = 2 → 3 → 4 → 5
# 2	2	3	2 → 1 → None	head = 3 → 4 → 5
# 3	3	4	3 → 2 → 1 → None	head = 4 → 5
# 4	4	5	4 → 3 → 2 → 1 → None	head = 5
# 5	5	None	5 → 4 → 3 → 2 → 1 → None


# 🔁 Dry Run on: head = [1 → 2 → 3 → 4 → 5 → None]
# Iteration	curr.val	next_node.val	prev list	List Progress
# Init	1	2	None	Original list
# 1	1	2	1 → None	1 reversed; rest unchanged
# 2	2	3	2 → 1 → None	2 reversed; 1 reversed
# 3	3	4	3 → 2 → 1 → None	3 reversed
# 4	4	5	4 → 3 → 2 → 1 → None	4 reversed
# 5	5	None	5 → 4 → 3 → 2 → 1 → None	Done

# Finally, return prev, which is now pointing to the new head (node 5).