class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def sub(i,res,store):
            res.add(tuple(set(store[:])))
            if i==len(nums):
                return 
            
            

            store.append(nums[i])
            sub(i+1,res,store)
            store.pop()
            sub(i+1,res,store)
        
        sub(0,res,[])
        return list(res)