#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.input:[1,1,2] 
# mag without duplicate[1,2]yeil tyachi length print karaychi.output: 2 nums = [1,2,_,_]

num = [1,1,2]
nums = []
thisset = set((num))
thislist = list((thisset))
for i in thislist:
    nums.append(i)
print(len(thislist), "," ,"nums =",nums)#both are not satisfy all condition

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        thisset = set((nums))
        thislist = list((thisset))
        return len(thislist)
result = Solution()
nums = [1,1,2]
ans = result.removeDuplicates(nums)
print(ans)


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         n = len(nums)
#         j = 1
#         for i in (1, n):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
# result = Solution()
# nums = [1,1,2]
# ans = result.removeDuplicates(nums)
# print(ans)