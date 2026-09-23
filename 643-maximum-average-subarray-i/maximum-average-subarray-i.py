class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = sum(nums[:k])
        max1 = total / k
        n = len(nums)
        j = 0
        for i in range(k , n):
            total -= nums[j] 
            total += nums[i]
            print(total)
            max1 = max(max1 , total / k)
            j += 1
        return max1