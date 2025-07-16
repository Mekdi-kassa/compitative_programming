class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        alt = 1
        prev = nums[0]
        if prev % 2 == 0:
            even += 1
        else:
            odd += 1
        
        for i in range(1 , len(nums)):
            if prev % 2 != nums[i] % 2:
                alt += 1
                prev = nums[i]
            if nums[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        return max(alt,odd , even)