# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# Example 1: Input: nums = [3,2,3]             Output: 3
# Example 2: Input: nums = [2,2,1,1,1,2,2]     Output: 2


nums = [3,2,3]
temp = {}
for i in nums:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
max_key = 0
max_value = float('-inf')
for key,value in temp.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key)

    

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        max_key = 0
        max_value = float('-inf')
        for key,value in temp.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key
result = Solution()
nums = [2, 2, 2, 1, 1, 1, 2]
max_key = result.majorityElement(nums)
print(max_key)



