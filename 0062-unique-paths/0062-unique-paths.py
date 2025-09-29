class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def unipa(i , j):
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     if i >= m or j >= n:
        #         return 0
            
        #     if (i, j) not in memo:
        #         memo[(i , j)] = unipa(i + 1,j) + unipa(i ,j +1)
        #     return memo[(i,j)]
        # return unipa(0,0) 
        
        
        dp = [[0] * n for _ in range(m)]
        dp[m -1][n -1] = 1
        for i in range(m -1,-1 ,-1):
            for j in range(n- 1, - 1,-1):
                if i == m -1 and j == n -1:
                    continue

                right_paths = dp[i][j+1] if j + 1 < n else 0
                bottom_paths = dp[i+1][j] if i + 1 < m else 0
            
                dp[i][j] = right_paths + bottom_paths
                
        return dp[0][0]