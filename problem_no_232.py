# 503. Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
# Example 1:
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

# Easy Algorithm Idea (Simple Version):
# Make res array of size n, all -1.
# Loop 2 times through the array (because it’s circular).
# Use a stack to store indices of elements.
# For each element from end to start:
# Remove elements from stack that are less than or equal to current.
# If stack is not empty, the top is the next greater.
# Save the result for that index.
# Push current element to stack.

def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        current = nums[i % n]

        while stack and stack[-1] <= current:
            stack.pop()

        if i < n:
            if stack:
                result[i] = stack[-1]
        
        stack.append(current)

    return result

print(nextGreaterElements([1, 2, 1]))
print(nextGreaterElements([1,2,3,4,3]))


# 🧠 Why i < n is needed:
# When we go through the array twice to simulate the circular behavior, the first n indices (i = 2n-1 to n) are just helping to fill the stack.

# But we only want to store results for the original elements at indices 0 to n-1, which means:

# Only update result[i] when i < n.
