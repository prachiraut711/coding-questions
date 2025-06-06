# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1: Input: s = "leetcode"     Output: 0
# Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.
# Example 2: Input: s = "loveleetcode"   Output: 2
# Example 3: Input: s = "aabb"     Output: -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        for index, char in enumerate(s):  #he Python enumerate function is a built-in utility that adds a counter to an iterable (like a list, string, or tuple) and returns it as an enumerate object. This object can then be iterated over to get both the index and the corresponding value of each item in the iterable.
            if char_count[char] == 1:
                return index
        return -1
    
result = Solution()
s = "leetcode"
ans = result.firstUniqChar(s)
print(ans)

# This loop iterates over the string s again, but this time it uses enumerate to get both:

# index: The current character's position in the string.
# char: The current character itself.
# For each character:

# Check if its count in char_count is 1 (meaning it is unique).
# If so, return the index of that character, because it’s the first unique character.