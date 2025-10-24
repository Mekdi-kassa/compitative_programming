class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """
        #adding to visted the point that we have changed
        row = len(matrix)
        col = len(matrix[0])
        vr = set()
        vc = set()
        # visted = set()
        # def inbound(r , c):
        #     if 0 <= r < row and 0 <= c < col and matrix[r][c] == 1:
        #         visted.add((r,c))
        #         matrix[r][c] = 0
        #     inbound(r + 1 , c)
        #     inbound(r - 1 , c)
        #     inbound(r , c + 1)
        #     inbound(r , c - 1)
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    vr.add(i)
                    vc.add(j)
        for i in range(row):
            for j in range(col):
                if i in vr or j in vc:
                    matrix[i][j] = 0
        
        