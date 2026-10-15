class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefix = [[0] *(self.col + 1) for _ in range(self.row + 1)]
        for i in range(self.row):
            for j in range(self.col):
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                ) 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row1][col1] + self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1]  - self.prefix[row2 + 1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)