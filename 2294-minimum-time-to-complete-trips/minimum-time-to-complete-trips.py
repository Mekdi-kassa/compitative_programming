class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        
        def trips_done(t: int) -> int:
            return sum(t // bus for bus in time)
        
        while left < right:
            mid = (left + right) // 2
            if trips_done(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left