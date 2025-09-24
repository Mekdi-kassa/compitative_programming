class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def trib(i):
            if i == 0:
                return 0
            
            if i == 1 or i == 2:
                return 1
            if i not in memo:
                memo[i]= trib(i - 1) + trib(i -2) + trib(i - 3)
            return memo[i]
        return trib(n)

            