class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runing_sum = 0
        ans = []
        for n in nums:
            runing_sum += n
            ans.append(runing_sum)
        return ans
        