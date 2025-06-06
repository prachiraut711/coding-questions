# You are given an array nums, where each number in the array appears either once or twice.
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
# Example 1: Input: nums = [1,2,1,3] Output: 1
# Explanation: The only number that appears twice in nums is 1.
# Example 2: Input: nums = [1,2,3] Output: 0
# Explanation: No number appears twice in nums.
# Example 3: Input: nums = [1,2,2,1] Output: 3
# Explanation: Numbers 1 and 2 appeared twice. 1 XOR 2 == 3.

nums = [1,2,2,1]
dict = {}
for i in nums:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)

result = 0
for i , j in dict.items():
    if j == 2:
        result ^= i

if result == 0:
    print("0")
else:
    print(result)
