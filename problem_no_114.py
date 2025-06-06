# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# Example 1: Input: s = "Hello"      Output: "hello"
# Example 2: Input: s = "here"        Output: "here"
# Example 3: Input: s = "LOVELY"      Output: "lovely"

s = "Hello"
s = s.lower()
print(s)

#APPROCH 2 WITHOUT USING BUILT IN FUNCTION (USING ASCII VALUE)
s = "LOVELY"
result = ''
for char in s:
    if "A" <= char <= "z":    #checks if the current character (char) is an uppercase letter. It does this by comparing the character to the range of uppercase letters ('A' to 'Z').
        result += chr(ord(char) + 32)
    else:
        result += char        #means if the character is not uppercase
print(result)

# ord(char) gets the ASCII value of the character char.
# Adding 32 to this value (ord(char) + 32) gives us the ASCII value of the corresponding lowercase letter.
# chr() is then used to convert this new ASCII value back into a character.
# result += chr(ord(char) + 32) adds the converted lowercase character to the result string.
# Why 32?:
# In the ASCII table, uppercase letters ('A' to 'Z') have values from 65 to 90, while lowercase letters ('a' to 'z') have values from 97 to 122.
# The difference between the uppercase and lowercase letters is always 32 (for example, 'A' is 65 and 'a' is 97; 'B' is 66 and 'b' is 98, etc.).