class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        l = 0
        ans = []
        r = n // 2
        for i in range(r , n):
            ans.append(nums[l])
            l += 1
            ans.append(nums[i])
        return ans

        