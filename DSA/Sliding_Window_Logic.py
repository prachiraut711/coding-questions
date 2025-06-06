#FIXED SLIDING WINDOW

nums = [5, 3, 1, -4, 7, 9]
k = 3
sum = 0
max_result = 0

for i in range(k):
    sum += nums[i]

max_result = sum

for i in range(k, len(nums)):
    sum += nums[i] - nums[i - k]
    max_result = max(max_result, sum)

print(max_result)