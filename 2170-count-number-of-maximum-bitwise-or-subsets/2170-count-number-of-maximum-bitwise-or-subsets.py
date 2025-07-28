class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subset(ans, store, ind):
            if ind == len(nums):
                ans.append(store)
                return
            subset(ans, store | nums[ind], ind + 1)

            subset(ans, store, ind + 1)

        ans = []
        subset(ans, 0, 0)
        max_or = max(ans)
        return ans.count(max_or)