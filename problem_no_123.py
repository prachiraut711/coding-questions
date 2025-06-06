# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to 
# eat the maximum number of different types of candies while still following the doctor's advice. Given the integer array candyType of 
# length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
# Example 1:   Input: candyType = [1,1,2,2,3,3]    Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
# Example 2:   Input: candyType = [1,1,2,3]   Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
# Example 3:   Input: candyType = [6,6,6,6]   Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType) // 2
        this_set = set(candyType)
        if len(this_set) > n:
            return n
        else:
            return len(this_set)
result = Solution()
candyType = [1,1,2,3]
ans = result.distributeCandies(candyType)
print(ans)

#APPROCH 2
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType) // 2
        this_set = set(candyType)
        return min(len(this_set), n)
result = Solution()
candyType = [6,6,6,6]
ans = result.distributeCandies(candyType)
print(ans)

#APPROCH 3
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        maxi=len(candyType)//2
        d={}
        for i in candyType:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=len(d)
        return min(l,maxi)
result = Solution()
candyType = [1,1,2,2,3,3]
ans = result.distributeCandies(candyType)
print(ans)


# but time limit exceeded so it will not submit
candyType = [1,1,2,3]
n = len(candyType) // 2
list1 = []
for i in candyType:
    if i not in list1:
        list1.append(i)
if len(list1) > n:
    print(n)
else:
    print(len(list1))






    