# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
# Example 1: Input: nums = [1,2,3,4]    Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2: Input: nums = [1,1,1,1,1]   Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3: Input: nums = [3,1,2,10,1]  Output: [3,4,6,16,17]

nums = [1,2,3,4]
thislist = []
for i in range(len(nums)):
    runningsum = 0
    for j in range(i + 1):
        runningsum += nums[j]
    thislist.append(runningsum)
print(thislist)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        thislist = []
        for i in range(len(nums)):
            runningSum = 0
            for j in range(i + 1):
                runningSum += nums[j]
            thislist.append(runningSum)
        return thislist
result = Solution()
nums = [3,1,2,10,1]
thislist = result.runningSum(nums)
print(thislist)

#approch 2
def runningSum(self, nums: list[int]) -> list[int]:
	runSum = [nums[0]] #our answer array starts with nums[0], which is the 0th running sum
	for i in range(1,len(nums)):
		runSum.append(runSum[i-1]+nums[i]) #the running sum up to index i is the sum of nums[i] and the running sum up to index i-1
	return runSum
result = Solution()
nums = [1, 1, 1, 1, 1]
thislist = result.runningSum(nums)
print(thislist)

# runSum starts as [1].
# For i = 1: The running sum is 1 (previous sum) + 1 (current element) = 2, so runSum = [1, 2].
# For i = 2: The running sum is 2 + 1 = 3, so runSum = [1, 2, 3].
# For i = 3: The running sum is 3 + 1 = 4, so runSum = [1, 2, 3, 4].
# For i = 4: The running sum is 4 + 1 = 5, so runSum = [1, 2, 3, 4, 5].
# The result is [1, 2, 3, 4, 5].
