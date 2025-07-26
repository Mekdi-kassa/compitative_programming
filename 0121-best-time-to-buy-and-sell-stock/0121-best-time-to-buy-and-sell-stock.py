class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_ = prices[0]
        
        for i in range(1, len(prices)):
            a = prices[i]
            prices[i] = max(prices[i] - min_,0)
            min_ = min(a,min_)
        if len(prices) == 1:
            return 0
        else:
            return max(prices[1:])