# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

s = "anagram"
t = "nagaram"
if sorted(s) == sorted(t):
    print(True)
else:
    print(False)



