class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo  = {}
        def coin(i ,ans):
            if ans == 0:
                return 0
            
            if i >= n:
                return float('inf')
            
            if ans < 0 :
                return float('inf')

            if (i , ans) not in memo:
                include = float('inf')
                #to keep what we have 
                if ans - coins[i] >= 0:
                    include = 1 + coin(i, ans - coins[i])
                # skip and go to the next without taking
                exclude = coin(i + 1,ans)
                memo[(i,ans)] = min(include,exclude)
            return memo[(i,ans)]

        res = coin(0,amount)
        if res != float('inf'):
            return res
        return -1