class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0 
        right = 1
        n = len(nums)
        while right < n:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
            