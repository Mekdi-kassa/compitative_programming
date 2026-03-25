class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        set1 = set()

        def dfs(r ,c , i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or c >= col  or r >= row or board[r][c]!= word[i] or (r,c) in set1):
                return False
            set1.add((r,c))
            res = dfs(r + 1 ,c ,i + 1) or dfs(r - 1 ,c ,i + 1) or dfs(r ,c + 1,i + 1) or dfs(r ,c - 1 ,i + 1)
            set1.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False