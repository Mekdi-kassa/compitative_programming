class Solution:
    def search(self, nums: List[int], target: int) -> int:
        set1 = set(nums)
        if target in set1:
            return nums.index(target)
        return -1