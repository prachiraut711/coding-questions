#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:  Input: s = "Let's take LeetCode contest"      Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:  Input: s = "Mr Ding"          Output: "rM gniD"




s = "Let's take LeetCode contest"
temp = s.split()
ans = []
for i in temp:
    rev_str = i[::-1]
    ans.append(rev_str)
result = ' '.join(ans)
print(result)