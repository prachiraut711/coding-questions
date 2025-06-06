# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where 
# it would be if it were inserted in order.You must write an algorithm with O(log n) runtime complexity.
# example 1: Input: nums = [1,3,5,6], target = 5     Output: 2
# Example 2: Input: nums = [1,3,5,6], target = 2     Output: 1
# Example 3: Input: nums = [1,3,5,6], target = 7     Output: 4
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i
result = Solution()
nums = [1,3,5,6] 
final = result.searchInsert(nums, 7)
print(final)      #but Time Complexity: o(nlogn)

#COEERCT APPROCH FOR O(logn)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
result = Solution()
nums = [1,3,5,6] 
final = result.searchInsert(nums, 7)
print(final)    #TIME COMPLEXIIY : O(logn)

# Initial State:[1,3,5,6] left = 0, right= 3
# left = 0, right = 3 (length of nums is 4, so right is 3).
# First Iteration:
# mid = (0 + 3) // 2 = 1
# nums[mid] = 3, which is less than target = 7, so update left = mid + 1 = 2.
# Second Iteration:
# mid = (2 + 3) // 2 = 2
# nums[mid] = 5, which is less than target = 7, so update left = mid + 1 = 3.
# Third Iteration:
# mid = (3 + 3) // 2 = 3
# nums[mid] = 6, which is less than target = 7, so update left = mid + 1 = 4.
# End of Loop:
# Now left = 4, which is greater than right = 3, so the loop ends.
# The method returns left = 4, which is the index where 7 should be inserted in the list [1, 3, 5, 6] to maintain the sorted order.
# Final Output
# The final output is 4, meaning the target value 7 should be inserted at index 4 in the list [1, 3, 5, 6].

# EXPLAINATION OF TIME COMPLEXITY.
# If we simply iterated over the entire array to find the target, the algorithm would run in O(n) time. We can improve this by using binary search
# instead to find the element, which runs in O(log n) time (see the video for a review of binary search).Now, why does binary search run in 
# O(log n) time? Well, with each iteration, we eliminate around half of the array. So now the question is: how many iterations does it take to
# converge on a single element? In other words, how many times do we need to divide n by 2 until we reach 1?
# If k is the number of times we need to divide n by 2 to reach 1, then the equation is:
# n / 2k = 1
# n = 2k   (multiply both sides by 2k)
# log2n = k   (definition of logarithms)
# So we know that it takes log2n steps in the worst case to find the element. But in Big O notation, we drop the base, so this ends up running in O(log n) time.
# If the target was not in the array, then we need to figure out what index the target would be at if it were inserted in sorted order.
# For a detailed visualization, please see the video (it's difficult to describe here) but basically, at the end of the loop, the left pointer 
# will have passed the right pointer (so l > r) and the target needs to be inserted between them. Inserting at index r actually ends up inserting
# the target at 1 spot behind the correct spot, so inserting at index l is the correct answer.