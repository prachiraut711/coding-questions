# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):
        max_element = 0
        for i in nums:
            if i > max_element:
                max_element = i

        count = [0] * (max_element + 1)

        for i in nums:
            count[i] += 1

        index = 0
        for i in range(len(count)):
            for _ in range(count[i]):    
                nums[index] = i
                index += 1    

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
            
        