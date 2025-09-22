class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2
            
            if i not in memo:
                memo[i] = climb(i-1) + climb(i-2)
            return memo[i]
        return climb(n)
        