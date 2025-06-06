#Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Example 1:  Input: nums = [1,2,3,1,1,3]  Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2: Input: nums = [1,1,1,1] Output: 6
# Explanation: Each pair in the array are good.
# Example 3: Input: nums = [1,2,3]  Output: 0

nums = [1,2,3,1,1,3]
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
print(count)

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
result = Solution()
nums = [1,1,1,1]
count = result.numIdenticalPairs(nums)
print(count)


#APPROACH 2
nums = [1,2,3,1,1,3]
temp = {}
for i in nums:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1   #temp = {1: 3, 2: 1, 3: 2}
ans = 0
for i in temp:
    ans += (temp[i] * (temp[i] - 1) // 2)  #Count how many times each number appears. If a number appears n times, 
                                           #then n * (n – 1) // 2 good pairs can be made with this number.
print(ans)       



#APPROCH 3
nums = [1,2,3,1,1,3]
thisset = set((nums))
count = 0
for i in thisset:
    temp = nums.count(i)
    count += (temp *(temp - 1) // 2)
print(count)

    



