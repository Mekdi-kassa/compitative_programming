class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * i for i in range(1,n + 1)]
        # def minsum(i , j):
        #     if i == n-1:
        #         return triangle[i][j]
        #     if i >= n or j >= n:
        #         return 0  
        #     if dp[i][j] == -1:
        #         p1 = triangle[i][j] + minsum(i + 1 ,j)
        #         p2 = triangle[i][j] + minsum(i + 1 ,j + 1)    
        #         dp[i][j] = min(p1,p2)
        #     return dp[i][j]
        # return minsum(0,0)
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = min(triangle[i][j] + dp[i-1][j-1],triangle[i][j] + dp[i-1][j])
        return min(dp[n-1])