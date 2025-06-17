# Given a string str, the task is to reverse it using stack. 
# Example:
# Input: s = "GeeksQuiz"
# Output: ziuQskeeG
# Input: s = "abc"
# Output: cba

def reverse(s):
    stack = []

    for i in s:
        stack.append(i)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str

print(reverse("abc")) 