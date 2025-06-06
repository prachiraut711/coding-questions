# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
# An alphanumeric string is a string consisting of lowercase English letters and digits.
# Example 1:
# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:
# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 

s = "dfa1111afd"
ans = []
for i in s:
    if i.isdigit():
        ans.append(int(i))
print(ans)

max = float("-inf")
second_max = float("-inf")

for i in ans:
    if max < i:
        second_max = max
        max = i
    elif second_max < i < max:  
        second_max = i


if second_max != float("-inf"):
    print(second_max)
else:
    print("-1")





