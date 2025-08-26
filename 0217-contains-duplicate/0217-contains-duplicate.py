class Solution(object):
    def containsDuplicate(self, nums): 
        num=set(nums)
        return len(num)!=len(nums)