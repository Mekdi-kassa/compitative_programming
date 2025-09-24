class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def unipa(i , j):
            if i == m-1 and j == n-1:
                return 1
            
            if i >= m or j >= n:
                return 0
            
            if (i, j) not in memo:
                memo[(i , j)] = unipa(i + 1,j) + unipa(i ,j +1)
            return memo[(i,j)]
        return unipa(0,0) 
