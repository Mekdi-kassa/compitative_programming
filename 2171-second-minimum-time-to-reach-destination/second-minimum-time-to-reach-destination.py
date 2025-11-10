class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n+1)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        INF = 10**30
        best = [[INF, INF] for _ in range(n+1)]
        best[1][0] = 0
        pq = [(0, 1)] 
        
        while pq:
            t, u = heapq.heappop(pq)
            if t > best[u][1]:
                continue
            
            if u == n and t == best[n][1]:
                return t
            
            for v in g[u]:
                depart = t
                cycles = depart // change
                if cycles % 2 == 1:
                    wait = change - (depart % change)
                    depart += wait
                arrive = depart + time
                
                if arrive < best[v][0]:

                    best[v][1] = best[v][0]
                    best[v][0] = arrive
                    heapq.heappush(pq, (arrive, v))
                elif best[v][0] < arrive < best[v][1]:
                    best[v][1] = arrive
                    heapq.heappush(pq, (arrive, v))
        
        return -1
