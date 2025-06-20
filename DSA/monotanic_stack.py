# MONOTANIC INCRESING STACK -A Monotonically Increasing Stack is a stack where elements are placed in increasing order from the bottom to the top. Example: 1, 3, 10, 15, 17

# Initialize an empty stack.
# Iterate through the elements and for each element:
# while stack is not empty AND top of stack is more than the current element
#  pop element from the stack
# Push the current element onto the stack.
# At the end of the iteration, the stack will contain the monotonic increasing order of elements.

def monotonicIncreasing(nums):
    stack = []

    for i in nums:
        while stack and stack[-1] > i:
            stack.pop() 
        stack.append(i)
    return stack

print(monotonicIncreasing([3, 1, 4, 1, 5, 9, 2, 6]))   #output = [1, 1, 2, 6]


#same code just constructed result array
def monotonicIncreasing(nums):
    stack = []
    result = []

    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is more than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element into the stack
        stack.append(num)

    # Construct the result array from the stack
    while stack:
        result.insert(0, stack.pop())

    return result

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicIncreasing(nums)
print("Monotonic increasing stack:", result)

#SEE NEXT SMALLER ELEMENT EXAMPLE FOR -1 TYPR QUESTION FOR MONTONIC INCREASING STACK.



# MONOTONIC DECRESING STACK: A Monotonically Decreasing Stack is a stack where elements are placed in decreasing order from the bottom to the top. Example: 17, 14, 10, 5, 1

# Start with an empty stack.
# Iterate through the elements of the input array.
# While stack is not empty AND top of stack is less than the current element:
# pop element from the stack
# Push the current element onto the stack.
# After iterating through all the elements, the stack will contain the elements in monotonic decreasing order.

def monotonicDecreasing(nums):
    stack = []

    for i in nums:
        while stack and stack[-1] < i:
            stack.pop()
        stack.append(i)

    return stack

print(monotonicDecreasing([3, 1, 4, 1, 5, 9, 2, 6]))  #output = [9,6]

#with constructed result array  (THIS IS IMP)
# 🔁 How It Works:
# You go through the array left to right.
# For each element:
# You remove any elements from the stack that are less than the current number, because they can't be the "nearest greater to the left" anymore.
# If the stack is not empty, the top element is the nearest greater to the left, so append it to result.
# If the stack is empty, it means no greater element to the left, so append -1.
# Push the current number onto the stack.

def monotonicDecreasing(nums):
    stack = []
    result = []

    for i in nums:
        while stack and stack[-1] < i:
            stack.pop()
        
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(i)
    
    return result

print(monotonicDecreasing([3,1,4,1,5,9,2,6]))  #output : result = [-1, 3, -1, 4, -1, -1, 9, 9]   stack will be = [9,6]


# 🔹 i = 0, num = 3
# Stack: [] (empty)
# No elements on the left → append -1 to result.
# Push 3 to stack.
# ➡️ result = [-1], stack = [3]
# 🔹 i = 1, num = 1
# Stack: [3]
# 3 > 1 → keep it. Nearest greater to left = 3
# Append 3 to result.
# Push 1 to stack.
# ➡️ result = [-1, 3], stack = [3, 1]
# 🔹 i = 2, num = 4
# Stack: [3, 1]
# 1 < 4 → pop
# 3 < 4 → pop
# Stack is now empty → append -1
# Push 4 to stack.
# ➡️ result = [-1, 3, -1], stack = [4]
# 🔹 i = 3, num = 1
# Stack: [4]
# 4 > 1 → Nearest greater to left = 4
# Append 4 to result.
# Push 1 to stack.
# ➡️ result = [-1, 3, -1, 4], stack = [4, 1]
# 🔹 i = 4, num = 5
# Stack: [4, 1]
# 1 < 5 → pop
# 4 < 5 → pop
# Stack is empty → append -1
# Push 5 to stack.
# ➡️ result = [-1, 3, -1, 4, -1], stack = [5]
# 🔹 i = 5, num = 9
# Stack: [5]
# 5 < 9 → pop
# Stack empty → append -1
# Push 9 to stack.
# ➡️ result = [-1, 3, -1, 4, -1, -1], stack = [9]
# 🔹 i = 6, num = 2
# Stack: [9]
# 9 > 2 → Nearest greater = 9
# Append 9
# Push 2 to stack
# ➡️ result = [-1, 3, -1, 4, -1, -1, 9], stack = [9, 2]
# 🔹 i = 7, num = 6
# Stack: [9, 2]
# 2 < 6 → pop
# Now top is 9 > 6 → keep it
# Append 9 to result
# Push 6 to stack
# ➡️ result = [-1, 3, -1, 4, -1, -1, 9, 9], stack = [9, 6]
