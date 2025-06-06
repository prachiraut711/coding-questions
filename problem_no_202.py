# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


#approch 1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = {}
        for i in ransomNote:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1


        freq2 = {}
        for i in magazine:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1


        for i, j in freq1.items():
            if freq2.get(i, 0) < j:
                return False
        return True
    
result = Solution()
ransomNote = "aa"
magazine = "ab"
ans = result.canConstruct(ransomNote, magazine)
print(ans)

#approch 2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list1 = list(magazine)
        for i in ransomNote:
            if i in list1:
                list1.remove(i)
            else:
                return False
        return True

# Creating object and testing
result = Solution()
ransomNote = "a"
magazine = "b"
ans = result.canConstruct(ransomNote, magazine)
print(ans)