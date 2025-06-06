nums = [1, 3, 5, 7, 9]
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
print(nums)