# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
# Example 1:
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.
# input : nums = [15]
# output:1


# from collections import Counter
# nums = [1,2,2,3,1,4]
# freq = Counter(nums)
# sum = 0
# for i in freq.values():
#     if i == max(freq.values()):
#         sum += i
# print(sum)



nums = [15]
freq = {}
for i in nums:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
sum = 0
for j in freq.values():
    if j == max(freq.values()):
        sum += j
print(sum)
        