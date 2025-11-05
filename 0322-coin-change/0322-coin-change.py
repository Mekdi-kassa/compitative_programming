class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dp(i , ans):
            if ans == 0:
                return 0
            
            if i >= n:
                return float('inf')

            if (i , ans) not in memo:
                include = float('inf')
                if ans - coins[i] >= 0:
                    include = 1 + dp(i , ans - coins[i])
                exclude = dp(i + 1 , ans)
                memo[(i , ans)] = min(include , exclude)
            return memo[(i ,ans)]
        ans = dp(0 ,amount)
        if ans != float('inf'):
            return ans
        return -1 
            
