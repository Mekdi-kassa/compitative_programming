class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = 1

        while left < right and right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                n = nums[left]
                nums[left] = nums[right]
                nums[right] = n
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                left += 1
                right += 1