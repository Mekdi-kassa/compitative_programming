class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        for i in range(len(mat)):
            ans.append((i,sum(mat[i])))
        
        ans.sort(key= lambda x: x[1])
        res = []
        for i in range(k):
            res.append(ans[i][0])
        return res