# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


nums = [1,2,3,2]
# dict = {}
# sum = 0
# for i in nums:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)
# for i, j in dict.items():
#     if j == 1:
#         sum += i
# print(sum)
sum = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] != nums[j] :
            sum += nums[i]
print(sum)