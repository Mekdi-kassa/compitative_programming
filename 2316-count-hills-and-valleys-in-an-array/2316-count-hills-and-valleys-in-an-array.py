class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        hill = 0
        valley = 0
        for i in range(1,n - 1):
            if nums[i] == nums[i-1]:
                continue
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            if left < 0:
                continue
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1
            if right >= n:
                continue 
            if nums[left] > nums[i] and nums[right]>nums[i]:
                hill += 1
            elif nums[left]<nums[i] and nums[right] < nums[i]:
                valley += 1
        return valley + hill


