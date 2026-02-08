from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=Counter(nums)
        for i in nums:
            if x[i]==1:
                return i
        
        