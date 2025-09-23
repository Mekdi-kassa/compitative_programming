class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[-1] * m for _ in range(n)]

        def dp (i , j):
            if i >= n or j >= m:
                return 0 
            
            if memo[i][j] == -1:
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + dp(i + 1 , j + 1)
                else:
                    memo[i][j] = max(dp(i ,j + 1) ,dp(i + 1 ,j))
            return memo[i][j]
        return dp(0,0)
        