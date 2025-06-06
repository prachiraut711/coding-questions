# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:0
# Input: nums = [3,3,3,3,3]
# # Output: 3

# approch1
nums = [1,3,4,2,2]
nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        print(nums[i])
        break

# approch2
nums = [3,1,3,4,2]
seen = set()
for i in nums:
    if i in seen:
        print(i)
    seen.add(i)


# but most optimal is  Floyd's Tortoise and Hare (Cycle Detection)  learn that.
