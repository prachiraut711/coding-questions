# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


nums = [1]
max_sum = float("-inf")
current_sum = 0
for i in nums:
    current_sum += i
    max_sum = max(max_sum, current_sum)
    if current_sum < 0:
        current_sum = 0
print(max_sum)



#  Kadane’s Algorithm Explanation :O(n) solution to find max sum of subarrays
# Initialize two variables:
# max_sum → Stores the maximum sum found so far.(max_sum = float(“-inf)
# current_sum → Stores the current subarray sum.(current_sum = 0)
# Iterate through the array:
# Add the current element to current_sum.
# Update max_sum if current_sum is greater.  (max_sum = max(max_sum, current_sum)
# If current_sum becomes negative, reset it to 0 (since a negative sum cannot contribute to the max sum).  (current_sum < 0 then current_sum = 0)



