# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

#O(n) solution
nums = [1,2,3,4]
left = []
for i in range(len(nums)):
    if i == 0:
        left.append(1)
    else:
        left.append(nums[i - 1] * left[-1])
print(left)

right = []
for i in range(len(nums)- 1, -1, -1):    #reverse range
    if i == len(nums) - 1:
        right.insert(0, 1)
    else:
        right.insert(0, nums[i + 1] * right[0])
print(right)

result = []
for i in range(len(nums)):
    result.append(left[i] * right[i])
print(result)



#O(n2) solution
nums = [1,2,3,4]
result = []
for i in range(len(nums)):
    mul = 1
    for j in range(len(nums)):
        if i != j:
            mul *= nums[j]
    result.append(mul)
print(result)