class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
     
        def rec(i):
            if memo[i] == -1:
                memo[i] = 1
                for j in range(i +1 ,n):
                    if nums[j] > nums[i]:
                        memo[i] = max(memo[i] , 1 + rec(j))
            return memo[i]

        max_val = 1
        for i in range(n):
            max_val = max(max_val , rec(i))
        return max_val



            
