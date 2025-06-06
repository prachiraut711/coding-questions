# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 
nums = [1,2,3,1,2,3]
k = 2
dict = {}
for i, j in enumerate(nums):
    if j in dict and abs(i - dict[j]) <= k:
        print(True)
    else:
        dict[j] = i
print(False)



# it shows time exceed limit
# if len(nums) < 2:
#     print(False)

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j]:
#             sub = abs(i - j)
#             if sub <= k:
#                 print(True)
#                 break
# print(False)


