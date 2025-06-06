# 628. Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# Example 1: Input: nums = [1,2,3]   Output: 6
# Example 2: Input: nums = [1,2,3,4]    Output: 24
# Example 3: Input: nums = [-1,-2,-3]   Output: -6


nums = [1,2,3,4,5,6,7]
nums.sort(reverse=True)
print(nums)
result = 1
for i in range(3):
    result *= nums[i]
print(result)

# wrong for other test cases