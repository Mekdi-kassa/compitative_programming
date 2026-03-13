class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def premutation(store,ans):
            if len(store) == len(nums):
                ans.append(store[:])
                return 
         
            for j in range(len(nums)):
                if nums[j] in store:
                    continue
                store.append(nums[j])
                premutation(store,ans)
                store.pop()
        ans=[]
        premutation([],ans)
        return ans