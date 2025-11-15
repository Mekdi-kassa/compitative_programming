class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]  
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return effort
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(heap, (next_effort, nr, nc))