#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

digits = [1, 2, 3]
num = ''
thislist = []
for i in digits:
    num += str(i)
    result = int(num) + 1
    ans = str(result)

for j in ans:
    thislist.append(int(j))
print(thislist)


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = ''
        thislist = []
        for i in digits:
            num += str(i)
            result = int(num) + 1
            ans = str(result)

        for j in ans:
            thislist.append(int(j))
        return thislist
com = Solution()
digits = [9]
thislist = com.plusOne(digits)
print(thislist)


