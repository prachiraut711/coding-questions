# 1047. Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)

print(removeDuplicates("abbaca"))



# Initialize an empty stack.

# For each character ch in the string:

# If the stack is not empty and the top of the stack equals ch, pop the top (remove both duplicates).

# Else, push ch to the stack.

# After the loop, return the characters in the stack joined as a string.