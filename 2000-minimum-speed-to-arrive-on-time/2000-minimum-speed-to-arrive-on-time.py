class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        
        left, right = 1, 10**7
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for d in dist[:-1]:
                time += math.ceil(d / mid)
            time += dist[-1] / mid
            
            if time <= hour:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans