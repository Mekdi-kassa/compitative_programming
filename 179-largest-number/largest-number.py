class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))

        def compare(m,n):
            if m + n > n + m:
                return -1
            elif m + n < n + m:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        if nums[0]=="0":
            return "0"
        
        return "".join(nums)