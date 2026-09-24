class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_dig(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        for i in range(len(nums)):
            if sum_dig(nums[i]) == i:
                return i
        return -1