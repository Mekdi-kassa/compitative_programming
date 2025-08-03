class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap=0
        for i in range(len(nums)-1):
            max_gap=max(max_gap,nums[i+1]-nums[i])
        return max_gap