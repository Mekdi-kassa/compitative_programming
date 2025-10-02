class Solution:
    def canCross(self, stones: List[int]) -> bool:

        n = len(stones)
        set1 = set(stones)
        memo = {}
        def frog(i ,last):
            if i == stones[-1]:
                return True
            
           
            if (i ,last) not in memo:
                res = False
                if (i + last + 1) in set1:
                    res = res or frog(i + last + 1,last + 1)
                if last - 1 > 0 and (i + last - 1) in set1:
                    res = res or frog(i + last - 1,last -1)
                
                if last > 0 and (i + last) in set1:
                    res = res or frog(i + last, last)
                
                memo[(i,last)] =res
            return memo[(i,last)]
        if stones[1] != 1:
            return False
        return frog(1,1)
