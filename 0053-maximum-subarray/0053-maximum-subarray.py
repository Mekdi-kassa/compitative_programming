class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1 = nums[0]
        runing_sum = 0
        for num in nums:
            if runing_sum < 0:
                runing_sum = 0
            runing_sum += num
            max1=max(max1,runing_sum)
        return max1