class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = {}
        for i, val in enumerate(nums):
            if val not in pos:
                pos[val] = []
            pos[val].append(i)
        
        ans = []
        for idx in queries:
            val = nums[idx]
            indices = pos[val]
            if len(indices) == 1:
                ans.append(-1)
                continue
            i = bisect_left(indices, idx)
            left = indices[i-1] if i > 0 else indices[-1] - n
            right = indices[i] if i < len(indices) and indices[i] != idx else indices[(i+1) % len(indices)]
            dist = min(abs(idx - left), (right - idx) % n)
            ans.append(dist)
        return ans