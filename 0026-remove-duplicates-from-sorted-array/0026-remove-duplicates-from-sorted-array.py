class Solution(object):
    def removeDuplicates(self, nums):
        let=[]
        for x in nums:
            if x not in let:
                let.append(x)
        nums[:]=let
        return len(nums)
        