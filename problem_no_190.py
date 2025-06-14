# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# approch 1
s = "A man, a plan, a canal: Panama"
ans = ""
for i in s:
    if "A" <= i <= "Z":
        i = chr(ord(i) + 32)
    if ("a" <= i <= "z") or ("0" <= i <= "9"):
        ans += i
if ans == ans[::-1]:
    print(True)
else:
    print(False)


# approch 2
s = "A man, a plan, a canal: Panama"
s = s.lower()
ans = ""
for i in s:
    if i.isalnum():
        ans += i
        
if ans == ans[::-1]:
    print(True)
else:
    print(False)