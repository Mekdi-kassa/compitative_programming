class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        mul = 1
        right = 0
        left = 0
        n = len(nums)
        count = 0
        if min(nums) > k:
            return 0
        while right < n:
            mul *= nums[right]
            while mul >= k and left < n:
                mul //= nums[left]
                left += 1
            count += (right - left + 1)
            right += 1
        return count