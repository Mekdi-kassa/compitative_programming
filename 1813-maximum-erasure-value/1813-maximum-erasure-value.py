class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        unique_elements = set()
        left = 0
        
        for right in range(len(nums)):
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            unique_elements.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        
        return max_sum