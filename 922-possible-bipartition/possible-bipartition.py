class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dict1 = defaultdict(list)
        for x , y in dislikes:
            dict1[x].append(y)
            dict1[y].append(x)
           
        color = [0] * (n+1)
       
        def dfs(node , par_col):
            if par_col == 1 :
                color[node] = 2
            else:
                color[node] = 1
           
            for nbr in dict1[node]:
                if not color[nbr]:
                    if not dfs(nbr,color[node]):
                        return False
                elif color[nbr] == color[node]:
                    return False
            return True
        
        for i in range(1,n+1):
            if color[i] == 0:
                if not dfs(i,1):
                    return False
        return True
             