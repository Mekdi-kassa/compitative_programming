class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def robber(ind):
            if ind == n -1:
                return nums[ind]
            if ind == n-2:
                return  max(nums[ind],nums[ind + 1])
            if ind not in memo:
                memo[ind] = max(nums[ind] + robber(ind + 2), robber(ind + 1))
            return memo[ind]
        return robber(0)