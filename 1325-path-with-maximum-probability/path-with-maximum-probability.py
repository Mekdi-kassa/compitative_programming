class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))  

        heap = [(-1.0, start_node)]  
        
        probs = [0.0] * n
        probs[start_node] = 1.0

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob  

            if node == end_node:
                return curr_prob

            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
