class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        memo = {}
        def dp(i,j):
            if j == len(s):
                return True
            
            if i >= n:
                return False
            
            if (i ,j) not in memo:
                include = False
                if t[i] == s[j]:
                    include = dp(i + 1 , j + 1)
                exclude = dp(i + 1, j)
                memo[(i,j)] = include or exclude
            return memo[(i,j)]
        return dp(0,0)