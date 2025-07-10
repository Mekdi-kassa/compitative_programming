class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sum1 = sum(nums) 
        # the right sum
        sum2 = 0
        # the left sum
        arr = []
        arr.append((0,sum1))
        l = 0
        while l < len(nums):
            if nums[l] == 0:
                sum2 += 1
            elif nums[l] == 1:
                sum1 -= 1
            arr.append((l + 1,sum1 + sum2))
            l += 1
        max_second = max(pair[1] for pair in arr)
        ans = []
        for x , y in arr:
            if y == max_second:
                ans.append(x)
        return ans
        
        