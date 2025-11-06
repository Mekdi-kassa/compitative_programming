class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
            if nums[i] > target:
                break
        return ans
