# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth
# that the richest customer has.A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the 
# customer that has the maximum wealth.
# Example 1: Input: accounts = [[1,2,3],[3,2,1]]   Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
# Example 2: Input: accounts = [[1,5],[7,3],[3,5]] Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
# Example 3: Input: accounts = [[2,8,7],[7,1,3],[1,9,5]  Output: 17

#approch1
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = float('-inf')
        for customer in accounts:     
            current_wealth = 0
            for amount in customer:
                current_wealth += amount
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        
        return max_wealth
result = Solution()
accounts = [[1,5],[7,3],[3,5]]
count = result.maximumWealth(accounts)
print(count)

#approch 2
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(customer) for customer in accounts)
result = Solution()
accounts = [[1,2,3],[3,2,1]]
count = result.maximumWealth(accounts)
print(count)

#approch 3
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            current_wealth = sum(account)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth
result = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
count = result.maximumWealth(accounts)
print(count)

        
        

        
