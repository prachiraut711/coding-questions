# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly t the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.
# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

#approch 1
nums = [1,7,3,6,5,6]

left = []
for i in range(len(nums)):
    if i == 0:
        left.append(i)
    else:
        left.append(nums[i - 1] + left[-1])
print(left)    #[0, 1, 8, 11, 17, 22]

right = []
for i in range(len(nums) -1, -1, -1):
    if i == len(nums) - 1:
        right.insert(0, 0)      #by taking zero instead of 1 we get same sum at same index
    else:
        right.insert(0, nums[i + 1] + right[0])
print(right)       #[27, 20, 17, 11, 6, 0]

found = False
for i in range(len(nums)):
    if left[i] == right[i]:
        print(i)
        found = True

if not found:
    print("-1")




#approch 2 but 0(n^2) bcz for loop O(n) and inside sum() = 0(n)
# nums = [1,7,3,6,5,6]
# found = False
# for i in range(len(nums)):
#     left = sum(nums[:i])
#     right = sum(nums[i + 1:])
#     if left == right:
#         print(i)
#         found = True
        
# if not found:
#     print("-1")



