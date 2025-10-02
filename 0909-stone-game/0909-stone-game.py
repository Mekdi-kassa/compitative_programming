class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}
        def winloss(i ,last):
            
            if i > last:
                return 0

            if (i ,last) not in memo:
                left_choose = piles[i] - winloss(i + 1,last)
                right_choose = piles[last] - winloss(i ,last -1)
                memo[(i,last)] = max(left_choose,right_choose)
            return memo[(i,last)]
        return winloss(0,n - 1) > 0