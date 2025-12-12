class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visted = [False] * len(isConnected)
        def dfs(city):
            for jcity in range(len(isConnected)):
                if isConnected[city][jcity] == 1 and  not visted[jcity]:
                    visted[jcity]=True
                    dfs(jcity)
        prov = 0
        for i in range(len(isConnected)):
            if not visted[i]:
                dfs(i)
                prov += 1
        return prov