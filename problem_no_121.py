# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:  Input: nums = [1,1,0,1,1,1]   Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:   Input: nums = [1,0,1,1,0,1]   Output: 2


nums = [1,0,1,1,0,1]
count = 0
max_count = 0
for i in nums:
    if i == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)
