#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays. Return the array ans.
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):   #2n length haviy mahnun 2 vela for loop run kel .[1,2,3,1,2,3] parat tech nums print karnysathi.
            for j in nums:
                ans.append(j)
        return ans
tt = Solution()
nums = [1,2,3]
ans = tt.getConcatenation(nums)
print(ans)

#approch 2
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)*2):
            ans.append(nums[i % len(nums)])
        return ans
tt = Solution()
nums = [1,2,3]
ans = tt.getConcatenation(nums)
print(ans)

#approch 3
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
tt = Solution()
nums = [1,2,3]
ans = tt.getConcatenation(nums)
print(ans)
