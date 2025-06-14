# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

prices = [7,1,5,3,6,4]
min_price = float("inf")
max_profit = 0
for i in prices:
    if i < min_price:
        min_price = i
    profit = i - min_price
    if profit > max_profit:
        max_profit = profit
print(max_profit)



# but it gives run time limit exeeds
prices = [7,1,5,3,6,4]
max_profit = 0
ans = []
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if prices[i] < prices[j]:
            max_profit = prices[j] - prices[i]
            ans.append(max_profit)
    
if not ans:
    print(0)
else:
    print(max(ans))
