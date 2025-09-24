class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}
        def pro(i,purchase):
            if i >= n:
                return 0

            if (i,purchase) not in memo:
                exclude = pro(i + 1, purchase)
                if purchase:
                    res = max(prices[i] + pro(i + 1,False) - fee , exclude)
                else:
                    res = max(exclude, -prices[i] + pro(i + 1 , True))
                memo[(i,purchase)] = res
            return memo[(i,purchase)]
        
        return pro(0,False)