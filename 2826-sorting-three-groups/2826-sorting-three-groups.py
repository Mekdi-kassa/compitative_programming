class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = dp2 = dp3 = 0
        
        for num in nums:
            if num == 1:
                dp1 = dp1 + 1
            elif num == 2:
                dp2 = max(dp1, dp2) + 1
            else: 
                dp3 = max(dp1, dp2, dp3) + 1
        
        return n - max(dp1, dp2, dp3)