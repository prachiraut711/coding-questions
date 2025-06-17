# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true


#approch 1
def isvalid(str):
    stack = []
    pairs = {")" : "(", "]" : "[", "}" : "{"}

    for i in str:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs:
            if stack[-1] != pairs[i]:
                return False
            stack.pop()

    return not stack

print(isvalid("[)]"))



#approch 2   This gives runtime error souse approch 1

def isvalid(str):
    # Declare a stack to store the opening brackets
    stack = []
    for i in range(len(str)):
        # Check if the character is an opening bracket
        if str[i] == "(" or str[i] == "{" or str[i] == "[":
            stack.append(str[i])
        else:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if stack and (stack[-1] == "(" and str[i] == ")") or (stack[-1] == "{" and str[i] == "}") or (stack[-1] == "[" and str[i] == "]"):
                # Pop the matching opening bracket
                stack.pop()

            else:
                # Unmatched closing bracket
                return False
    # If stack is empty, return True (valid), otherwise False
    return not stack
    
print(isvalid("(){}[]"))
                                                                                                            