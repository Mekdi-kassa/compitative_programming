class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        count = 1
        last = points[0][1] 
        for st, end in points[1:]:
            if st > last:
                count += 1
                last = end
        return count
