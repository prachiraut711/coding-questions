# Nearest smaller numbers on LEFT SIDE in an array
# Given an array of integers, find the nearest smaller number for every element such that the smaller element is on the left side.
# Examples: 
# Input: arr = [1, 6, 2]
# Output: [-1, 1, 1,]
# Explanation: There is no number at the left of 1. Smaller number than 6 and 2 is 1.

# Input: arr = [1, 5, 0, 3, 4, 5]
# Output: [-1, 1, -1, 0, 3, 4]
# Explanation: Upto 3 it is easy to see the smaller numbers. But for 4 the smaller numbers are 1, 0 and 3. But among them 3 is closest. Similarly for 5 it is 4.

def find_next_smaller_element(arr):
    stack = []
    result = []

    for i in arr:
        while stack and stack[-1] >= i:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(i)

    return result

print(find_next_smaller_element([1, 6, 2]))
print(find_next_smaller_element([1, 5, 0, 3, 4, 5]))