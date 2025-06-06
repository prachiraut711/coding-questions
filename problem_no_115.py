# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Example 1:  Input: s = "Hello, my name is John"   Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:  Input: s = "Hello"     Output: 1


class Solution:
    def countSegments(self, s: str) -> int:
        ans = s.split()
        return len(ans)
result = Solution()
s = "Hello, my name is John"
ans = result.countSegments(s)
print(ans)