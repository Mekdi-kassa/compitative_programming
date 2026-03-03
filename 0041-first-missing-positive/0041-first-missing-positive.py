class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        for i in range(1,len(nums)+2):
            if i not in nums:
                return i
        return 1