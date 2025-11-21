class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dict1 = defaultdict(list)
        i = 0
        for source , distination in equations:
            dict1[source].append([distination,values[i]])
            dict1[distination].append([source,1/values[i]])
            i+=1
       
        
        def dfs(node,distionation,v):
            if node == distionation:
                return v
            visted.add(node)
            for i,val in dict1[node]:
                if i not in visted:
                    x = dfs(i,distionation,v*val) 
                    if x != -1: 
                        return x
            return -1
        res = []

        for  source , destionation in  queries:
            visted = set()
            if source not in dict1 or destionation not in dict1:
                res.append(-1)
            else:
                res.append(dfs(source,destionation,1))
        return res


            
            