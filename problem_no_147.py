# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
# Example 1:
# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.
# Example 2:
# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.
# Example 3:
# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

dic_1={}
dic_2={}

for i in words1:
    if i not in dic_1:
        dic_1[i]=1
    else:
        dic_1[i]+=1

for j in words2:
    if j not in dic_2:
        dic_2[j]=1
    else:
        dic_2[j]+=1

set_1=set()
set_2=set()

for i,j in dic_1.items():
    if j==1:
        set_1.add(i)

for i,j in dic_2.items():
    if j==1:
        set_2.add(i)

print(len(set_1.intersection(set_2)))      