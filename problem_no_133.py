# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Example 1:  Input: nums = [4,3,2,7,8,2,3,1]     Output: [5,6]
# Example 2:  Input: nums = [1,1]     Output: [2]

nums = [1,1]
result = list(range(1, len(nums)+1))
for i in range(len(nums)):
    if nums[i] in result:
        result.remove(nums[i])
print(result)

#but it gives time limit exeed error.