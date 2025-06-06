#You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.
# Example 1: Input: nums = [1,2,3,4]  Output: 3
# Explanation: All array elements can be made divisible by 3 using 3 operations
# Subtract 1 from 1.# Add 1 to 2.# Subtract 1 from 4.
# Example 2:  Input: nums = [3,6,9]    Output: 0

nums = [17, 18, 19 , 20]
ans = []
for i in nums:
    ans.append(i % 3)   #ans =[2,0,1,2] output al remainder 
count = 0
for j in ans:
    if j == 1 or j == 2:
        count += 1
print(count)

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            ans.append(i % 3)   # i%3 ni 0,1,2,3 ch remainder yetat .mag 0 ani 3 la kahich operation karaychi garaj nahi yanch operation= 0
        count = 0               # pn 1 ani 2 madhe 3 chya shejari 2 mag 2+1=3  1 operation vaprl mag 1 ala reamainder tar thithe operation = 1
        for j in ans:           # pn 0 chya shejari 1 mag 1 opeartion so jevva 1 yeil tevva operation = 1
            if j == 1 or j == 2:
                count += 1
        return count
result = Solution()
nums = [17, 18, 19 , 20]
count = result.minimumOperations(nums)
print(count)


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            temp = i % 3
            if temp == 1 or temp == 2:
                count += 1
        return count
result = Solution()
nums = [3, 6, 9]
count = result.minimumOperations(nums)
print(count)
