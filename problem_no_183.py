# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
# Note: The boy can buy the ice cream bars in any order.
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# You must solve the problem by counting sort.
# Example 1:
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
# Example 2:
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
# Example 3:
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
costs = [1,3,2,4,1] 
coins = 7
costs.sort()
temp = 0
for i in costs:
    coins -= i
    if coins >= 0:
        temp += 1
    else:
        break
print(temp)

#using counting sort
costs = [1,3,2,4,1]
coins = 7
max_element = 0
for i in costs:
    if i > max_element:
        max_element = i

count = [0] * (max_element + 1)
for i in costs:
    count[i] += 1

sorted_arr =[]
for i in range(len(count)):
    for _ in range(count[i]):
        sorted_arr.append(i)

temp = 0
for i in sorted_arr:
    coins -= i
    if coins >= 0:
        temp += 1
    else:
        break
print(temp)


    