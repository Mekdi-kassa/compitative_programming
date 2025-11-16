# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        while high>=low:
            mid=(low+high)//2
            if not isBadVersion(mid):
                low=mid+1    
            else:
                high=mid-1
        return high+1