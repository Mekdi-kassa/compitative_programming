class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = sum(nums[:k])
        max1 = total
        n = len(nums)
        j = 0
        for i in range(k , n):
            total -= nums[j] 
            total += nums[i]
            max1 = max(max1 , total)
            j += 1
        return max1 / k