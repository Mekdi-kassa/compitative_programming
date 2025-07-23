class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s=float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                val= nums[i]+nums[left]+nums[right]
                if val==target:
                    return val
                elif val>target:
                    right-=1
                else:
                    left+=1
                if abs(target-val)<abs(target-s):
                    s=val
        return s
