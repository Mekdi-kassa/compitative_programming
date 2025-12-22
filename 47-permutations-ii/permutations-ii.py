class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permu(i,store,ans):
            if i == len(nums):
                ans.add(tuple(nums[:]))
            for j in range(i,len(nums)):
                store.add(nums[i])
                nums[i],nums[j]=nums[j],nums[i]
                permu(i+1,store,ans)
                nums[i],nums[j]=nums[j],nums[i]
        ans=set()
        set1=set()
        permu(0,set1,ans)
        return list(ans)