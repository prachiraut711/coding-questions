class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i, j in zip(s,t):
            if i in dict1:
                if dict1[i] != j:
                    return False
            else:
                dict1[i] = j
            if j in dict2:
                if dict2[j] != i:
                    return False
            else:
                dict2[j] = i
        return True
       
result = Solution()
s =  "egg"
t = "add"
ans = result.isIsomorphic(s,t)
print(ans)