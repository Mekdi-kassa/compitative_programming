class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #toplogy
        dict1 = defaultdict(list)
        dict2 = defaultdict(int)

        for x , y in edges:
            dict1[x].append(y)
            dict2[y] += 1
        
        que = deque([])
        ans = [[] for _ in range(n)]
       
        for i in range(n):
            if dict2[i] == 0:
                que.append(i)
        

        
        while que:
            node = que.popleft()
            for nbr in dict1[node]: 
                ans[nbr].append(node)
                ans[nbr].extend(ans[node])
                y = list(set(ans[nbr]))
                y.sort()
                ans[nbr] = y
                dict2[nbr] -= 1
                if dict2[nbr] == 0:
                    que.append(nbr)
        return ans

    
    