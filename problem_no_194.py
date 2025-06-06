# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# approch 1
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums 

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(nums)
reverse(nums, 0, len(nums) - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, len(nums) - 1)
print(nums)


# approch 2
nums = [1,2,3,4,5,6,7]
k = 3
k = k % len(nums)
nums = nums[-k:] + nums[:-k]
print(nums)


