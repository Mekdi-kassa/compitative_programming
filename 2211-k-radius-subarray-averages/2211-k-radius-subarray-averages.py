from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1) 
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        res = [-1] * n
        window_size = 2 * k + 1
        
        for i in range(n):
            if i - k >= 0 and i + k < n:
                window_sum = prefix[i + k + 1] - prefix[i - k]
                res[i] = window_sum // window_size
        return res