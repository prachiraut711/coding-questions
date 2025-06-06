# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.
# Example 1:
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.


s = "abcaca"
count = {}
temp = []
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for j in count:
    if count[j] >= 2:
        temp.append(j)

if len(temp) <= 0:
    print("-1")
else:
    ans = []
    for p in temp: 
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != p:
                i += 1
            if s[j] != p:
                j -= 1
            if s[i] == p and s[j] == p:
                ans.append(j - i -1)
                i += 1
                j -= 1
    print(max(ans))
            




















# dict = {}
# for i, j in enumerate(s):
#     if j not in dict:
#         dict[j] = i
#     else:
#         len = i - dict[j] - 1
# print(len)


