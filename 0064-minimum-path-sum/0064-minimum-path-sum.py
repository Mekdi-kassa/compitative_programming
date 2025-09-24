class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        memo = {}
        def minsum(i ,j):
            if i >= row or j >= col:
                return float('inf')
            if i == row -1 and j == col -1:
                return grid[i][j]
            
            if (i,j) not in memo:
                memo[(i,j)] = min(grid[i][j] + minsum(i ,j+1) ,grid[i][j] + minsum(i + 1 ,j))
            return memo[(i,j)]
        return minsum(0,0)
            