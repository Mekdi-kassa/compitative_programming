class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        #graph buliding
        graph = defaultdict(list)
        in_deg = defaultdict(int)
        for x , y in edges:
            graph[x].append(y)
            graph[y].append(x)
            in_deg[x] += 1
            in_deg[y] += 1
        
        que = deque([])
        for i in range(n):
            if in_deg[i] == 1:
                que.append(i)


        res = set()
        while n > 2:
            n -= len(que)
            for _ in range(len(que)):
                node = que.popleft()
                for nbr in graph[node]:
                    in_deg[nbr] -= 1
                    if in_deg[nbr] == 1:
                        que.append(nbr)
        return list(que)


        
        
        