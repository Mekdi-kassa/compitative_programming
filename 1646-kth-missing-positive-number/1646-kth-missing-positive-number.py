class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max1 = max(arr)
        set1 = set(arr)
        j = 0
        
        for i in range(1 , max1 + 1 + k):
            if i not in set1:
                j += 1
            if j == k:
                return i
        return -1 
