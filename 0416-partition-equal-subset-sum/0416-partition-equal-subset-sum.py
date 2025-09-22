class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = sum(nums)
        if sum1 % 2 != 0:
            return False
        target = sum1 // 2
        n = len(nums)
        @cache 
        def back(i,ans):
            if  ans == target:
                return True
            if ans > target:
                return False
            if i > n - 1:
                return False
            
            return back(i + 1, ans+nums[i]) or back(i + 1 , ans)
        return back(0 ,0)

