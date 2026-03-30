class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset2(i,ans,store):
            m=sorted(store)
            ans.add(tuple(m[:])) 
            if i == len(nums):
                return 
            store.append(nums[i])
            subset2(i+1,ans,store)
            store.pop()
            subset2(i+1,ans,store)

            
        
        ans=set()
        subset2(0,ans,[])
        return list(ans)