# Given array contain 1 and 0, put all 1 on left side and 0 on right side of the array
nums = [1 ,0 ,0 ,0, 1, 1, 1 ,0 ,1, 0]
for i in nums:
    if i == 0:
        nums.remove(0)
        nums.append(0)
print(nums)        #output will be [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]