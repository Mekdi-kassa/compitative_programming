class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l = n - 2
        memo = {}
        def fib(i):
            if i == len(nums) -1:
                return nums[i]
            if i == len(nums) -2:
                return max(nums[i],nums[i + 1])
            
            if i not in memo:
                memo[i] = max(nums[i] + fib(i + 2),fib(i + 1 ))
            return memo[i]
        ans = fib(1)
        nums.pop()
        memo ={}
        ans2 = fib(0)
        return max(ans , ans2)
            

        