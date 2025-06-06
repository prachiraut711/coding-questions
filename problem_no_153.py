# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.
# Example 1:
# Input: s = "hello"
# Output: 13
# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
# Example 2:
# Input: s = "zaz"
# Output: 50
# Explanation:
# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.


s = "hello"
sum = 0
for i in range(len(s) - 1):  #bcz last la i = o mag i + 1 nahiyech pusdhe kahi mahnun l paryantch loop getl mag i + 1 = o zala
    sum += abs(ord(s[i]) - ord(s[i + 1]))   
print(abs(sum))

# To convert a string into ASCII values in Python, you can use the ord() function for each character.
# To prevent negative values in Python, you can use the built-in abs() function, which returns the absolute (non-negative) value of a number. 