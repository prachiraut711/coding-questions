nums = [1,2,2,3]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i <= j and(nums[i] <= nums[j] and nums[i] >= nums[j]):
            print(True)
        else:
            print(False)