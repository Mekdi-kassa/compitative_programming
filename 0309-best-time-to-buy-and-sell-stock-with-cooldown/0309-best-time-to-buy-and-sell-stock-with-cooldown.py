class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo ={}
        def profit(i , purchase,cooldown):
            if i >= n:
                return 0

            if (i , purchase ,cooldown) not in memo:
                if cooldown:
                    res = profit(i + 1, purchase , False) 
                else:
                    exclude = profit(i + 1 , purchase , cooldown)

                    if purchase:
                        res = max(exclude , prices[i] + profit(i+1,False,True))
                    elif not purchase:
                        res = max(exclude , -prices[i] + profit(i+1,True,False))

                
                memo[(i,purchase,cooldown)] = res
            return memo[(i,purchase,cooldown)]
        return profit(0,False,False)