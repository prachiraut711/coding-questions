# 796. Rotate String
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

def is_cyclic(s, goal):
    if len(s) != len(goal):
        return False
    
    temp = s + s
    if goal in temp:
        return True
    else:
        return False


print(is_cyclic("abc", "bca"))  #true
print(is_cyclic("abcd", "acbd"))  # False
print(is_cyclic("ab", "a"))  #false