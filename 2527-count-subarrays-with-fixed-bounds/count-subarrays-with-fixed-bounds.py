class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left_bound = 0
        last_min = -1
        last_max = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i+1
                last_min = -1
                last_max = -1
                continue
            if nums[i]==minK:
                last_min = i
            if nums[i]==maxK:
                last_max = i


            if last_min != -1 and last_max != -1:
                count += max(0, min(last_min, last_max) - left_bound + 1)
        return count
