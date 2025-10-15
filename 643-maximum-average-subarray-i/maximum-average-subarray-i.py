class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = sum(nums[:k])
        max1 = sum1 /k 
        j = 0
        for i in range(k , len(nums)):
            sum1 -= nums[j]
            sum1 += nums[i]
            val = sum1 /k
            max1 = max(max1 , val)
            j += 1
        return max1