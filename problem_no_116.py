#We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".

# Given a string word, return true if the usage of capitals in it is right.
# Example 1: Input: word = "USA"  Output: true
# Example 2: Input: word = "FlaG" Output: false


word = "Google"
if word.isupper():
    print(True)
elif word.islower():
    print(True)
elif word[0].isupper() and word[1:].islower():
    print(True)
else:
    print(False)



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
result = Solution()
word = "FlaG"
ans = result.detectCapitalUse(word)
print(ans)

         

