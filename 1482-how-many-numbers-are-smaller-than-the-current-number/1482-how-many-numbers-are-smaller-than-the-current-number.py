class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [(nums[i],i) for i in range(len(nums))]
        arr.sort(key = lambda x:x[0])
        n = len(nums)
        ans = [0] * n
        prev_num = None
        prev_count = 0
        for i in range(n):
            num , j = arr[i] 
            if num != prev_num:
                prev_count = i  
                prev_num = num
            ans[j] = prev_count
        return ans

        
