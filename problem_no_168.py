# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

nums = [2,2,3,2]
dict = {}
for i in nums:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i, j in dict.items():
    if j == 1:
        print(i)