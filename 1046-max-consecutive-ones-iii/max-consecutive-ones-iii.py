class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        right = 0
        left = 0
        n = len(nums)
        dict1 = defaultdict(int)
        count = 0
        while right < n:
            dict1[nums[right]] += 1
            while nums[right] == 0 and dict1[nums[right]] > k:
                dict1[nums[left]] -= 1
                left += 1
            count = max(count , (right - left + 1))
            right += 1
        return count
