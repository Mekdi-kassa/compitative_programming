class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k):
            left = 0 
            right = 0 
            n = len(nums)
            res = 0 
            dict1 = defaultdict(int)
            while right < n:
                dict1[nums[right]] += 1
                while len(dict1) > k:
                    dict1[nums[left]] -= 1
                    if dict1[nums[left]] == 0:
                        dict1.pop(nums[left])
                    left += 1
                res += (right - left + 1)
                right += 1
            return res
        
        return atmost(k) - atmost(k-1)
