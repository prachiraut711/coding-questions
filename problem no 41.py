# Define two integers, num1 and num2, as follows:num1: The sum of all integers 
# in the range [1, num + 1] that are not divisible by num2.
# num2: The sum of all integers in the range [1, num1 + 1] that are divisible by num2.
# Return the integer num1 - num2
#Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.

num1 = 10 
num2 = 3
sum1 = 0
sum2 = 0

for i in range(1, num1 + 1): 
    if i % num2 != 0:
        sum1 += i
print("Sum of num that are not divisible by num2:",sum1)

for i in range(1, num1 +1):
    if i % num2 == 0:
        sum2 += i
print("Sum of num that are divisible by num2:",sum2)
result = sum1 - sum2
print(result)
