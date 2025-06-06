# Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
# Example 1:  Input: pattern = "abba", s = "dog cat cat dog"   Output: true
# Explanation: The bijection can be established as: 'a' maps to "dog".  b' maps to "cat".
# Example 2:  Input: pattern = "abba", s = "dog cat cat fish"   Output: false
# Example 3:  Input: pattern = "aaaa", s = "dog cat cat dog"   Output: false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()     #["dog", "cat", "cat", "dog"].
        if len(pattern) != len(words):     #If the length of pattern doesn't match the length of words, the function returns False right away
            return False
        
        char_to_word = {}   #This dictionary will map each character in pattern to a unique word in words.
        word_to_char = {}   #This dictionary will map each word in words to a unique character in pattern.
        
        for char, word in zip(pattern, words):    #zip(pattern, words) produces pairs: [('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')].zip(pattern, words) pairs each character in pattern with each word in words.
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
result = Solution()
pattern = "abba"
s = "dog cat cat dog"
ans = result.wordPattern(pattern,s)
print(ans)
      
# Splitting s into words:
# words = ["dog", "cat", "cat", "dog"]
# Length Check:
# Both pattern and words have a length of 4, so the function continues.
# Iteration and Mappings:
# For the first pair ('a', 'dog'):
# char_to_word = {'a': 'dog'}
# word_to_char = {'dog': 'a'}
# For the second pair ('b', 'cat'):
# char_to_word = {'a': 'dog', 'b': 'cat'}
# word_to_char = {'dog': 'a', 'cat': 'b'}
# For the third pair ('b', 'cat'):
# Both char_to_word['b'] and word_to_char['cat'] are consistent with previous mappings.
# For the fourth pair ('a', 'dog'):
# Both char_to_word['a'] and word_to_char['dog'] are consistent with previous mappings.
# Returning True:
# Since all pairs are consistent with the one-to-one mapping, the function returns True.
# This solution checks if s follows the pattern, ensuring a unique and consistent mapping between letters and words.









