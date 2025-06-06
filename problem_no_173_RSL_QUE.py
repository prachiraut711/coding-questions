# to get last digit without using in built function
num = 121
ans = num % 10
print(ans)

# to get sum of digit without using in built function
num = 4721
while num > 9:
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    num = sum
print(sum)










