class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max1 = max(nums)
        min1 = min(nums)

        ans = 0
        for i in range(1, min1 + 1):
            if max1 % i == 0 and min1 % i == 0:
                ans = max(ans , i)
        return ans