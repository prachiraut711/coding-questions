#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with
#a linear runtime complexity and use only constant extra space.
# Example 1: Input: nums = [2,2,1]       Output: 1
# Example 2: Input: nums = [4,1,2,1,2]   Output: 4
# Example 3: Input: nums = [1]           Output: 1
 
nums = [2,2,1]    #by using XOR gate
result = 0        #in xor 1 1 = 0, 0 0 = 0 (same aslyvar 0) nahitar 0 1 = 1, 1 0 = 1
for i in nums:
    result ^= i
print(result)


#method 1
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
ans = Solution()
nums = [4,1,2,1,2]
result = ans.singleNumber(nums)
print(result)

#x ⊕ x = 0 for any number  𝑥 ⊕ 0=𝑥  x ⊕ 0 = x.
# Initial state: result = 0  Array: [4, 1, 2, 1, 2]
# XOR step by step:
# XOR result with the first element (4): 𝑟𝑒𝑠𝑢𝑙𝑡 = 0 ⊕ 4 = 4 result = 0 ⊕ 4 = 4   (he sagl binary madhye kar mahnhe 1 = 0001,2=0010 mag tyach ans yeil tyach decimal lihi.)
# Now, result = 4.                                                        (ithe 0 = 0000, 4 = 0001 mag yach ans 0001 al mahnhe 4.)
# XOR result with the second element (1): 𝑟𝑒𝑠𝑢𝑙𝑡 = 4 ⊕ 1 = 5 result = 4 ⊕ 1 = 5
# Now, result = 5.
# XOR result with the third element (2): result = 5 ⊕ 2 = 7 result = 5 ⊕ 2 = 7
# Now, result = 7. 
# XOR result with the fourth element (1): result = 7 ⊕ 1 = 6 result = 7 ⊕ 1 = 6
# Now, result = 6. 
# XOR result with the fifth element (2): result = 6 ⊕ 2 = 4 result = 6 ⊕ 2 = 4
# Now, result = 4.
# Final result: After all XOR operations, result = 4, which is the single number in the array that appears only once.