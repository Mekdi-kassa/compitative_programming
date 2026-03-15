class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # for this question we must take that specific row and colomn to be changed 
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        def check(row , col):
            if row < 0 or col < 0 or col >= len(board[0]) or row >= len(board) or board[row][col] == "X" or board[row][col] == "T":
                return
            
            board[row][col] = "T"
            check(row - 1,col)
            check(row + 1,col)
            check(row ,col + 1)
            check(row, col - 1)
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or i == len(board)-1 or j == 0 or j == len(board[0]) -1) and board[i][j] == "O":
                    check(i, j)
        
      
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"  
                elif board[i][j] == "T":
                    board[i][j] = "O"  