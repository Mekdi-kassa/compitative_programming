class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def mincost(i):
            if i == n - 1:
                return cost[i]
            
            if i >= n:
                return 0


            if i not in memo:
                memo[i] = cost[i] + min(mincost(i + 1),mincost(i + 2))
            return memo[i]
        return min(mincost(0),mincost(1))