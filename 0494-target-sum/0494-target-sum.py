class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = {}
        def back(i ,ans):

            if i == n:
                if ans == target:
                    return 1 
                else:
                    return 0
            if (i ,ans) not in memo:
                memo[(i,ans)] = back(i + 1,ans + nums[i]) + back(i + 1, ans - nums[i]) 
            return memo[(i,ans)]   
        return back(0,0)
        
                

                