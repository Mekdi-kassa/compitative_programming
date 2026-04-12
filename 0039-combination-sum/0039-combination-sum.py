class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combsum(i,ans,store,total):
            if total == target:
                ans.append(store[:])
                return 

            if i == len(candidates) or total > target:
                return 
            
            store.append(candidates[i])
            combsum(i,ans,store,total+candidates[i])
            store.pop()
            combsum(i+1,ans,store,total)

        ans=[]
        combsum(0,ans,[],0)
        return ans

