class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrow(board): 
            for i in range(len(board)):
                arr = []
                for j in range(len(board[i])):
                    if board[i][j] != ".":
                        if board[i][j] in arr:
                            return False
                        arr.append(board[i][j])
            return True

        def checkcol(board):
            for i in range(len(board[0])):
                arr = []
                for j in range(len(board)):
                    if board[j][i] != ".":
                        if board[j][i] in arr:
                            return False
                        arr.append(board[j][i])
            return True

        def girdcheck(board):
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    seen = set()
                    for r in range(row, row + 3):
                        for c in range(col, col + 3):
                            if board[r][c] != ".":
                                if board[r][c] in seen:
                                    return False
                                seen.add(board[r][c])
            return True

        return checkrow(board) and checkcol(board) and girdcheck(board)