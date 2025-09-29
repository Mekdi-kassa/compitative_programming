class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = len(coins)
        # memo  = {}
        # def coin(i ,ans):
        #     if ans == 0:
        #         return 1       
        #     if i >= n or ans < 0:
        #         return 0
        #     if (i , ans) not in memo:
        #         include = 0
        #         #to keep what we have 
        #         if ans - coins[i] >= 0:
        #             include = coin(i, ans - coins[i])
        #         # skip and go to the next without taking
        #         exclude = coin(i + 1,ans)
        #         memo[(i,ans)] = include + exclude
        #     return memo[(i,ans)]
        # return coin(0,amount)
        dp = [[0] *(amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(len(coins) - 1 , - 1, -1):
            for j in range(amount + 1):
                
                dp[i][j] = dp[i + 1][j]
                
                if j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]]
        return dp[0][amount]

