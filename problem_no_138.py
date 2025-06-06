# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        freqOfNumberDict = {}
        storeKey = []
        ans = []
        lastIndex = 0
        firstIndex = 0

        # Created dict with freq of element
        for i in nums:
            if i not in freqOfNumberDict:
                freqOfNumberDict[i] = 1
            else:
                freqOfNumberDict[i] += 1

        # Sorted dict
        sortedFreqDict = sorted(freqOfNumberDict.items(), key=lambda x:x[1], reverse = True)
        
        # max freq
        max = sortedFreqDict[0][1]
        
        # Stored keys.
        for i,j in sortedFreqDict:
            if max <= j:
               storeKey.append(i) 
        
        for i in storeKey:
            left = 0
            right = len(nums) - 1

            while left <= right :
                if nums[right] == i:
                    lastIndex = right
                    break
                right -= 1
            
            while left <= right :
                if nums[left] == i:
                    firstIndex = left
                    break
                left += 1
            ans.append(lastIndex - firstIndex + 1)
        return min(ans)
result = Solution()
nums = [1,2,2,3,1]
temp = result.findShortestSubArray(nums)
print(temp)
        