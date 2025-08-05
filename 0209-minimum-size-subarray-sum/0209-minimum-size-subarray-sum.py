class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            minleng = float('inf')
            sum1 = 0
            n = len(nums)
            count = 0
            left = 0
            for i in range(n):
                sum1 += nums[i]
                count += 1
                while sum1 >= target:
                    minleng = min(minleng ,count)
                    sum1 -= nums[left]
                    left += 1
                    count -= 1
                    
            if minleng == float('inf'):
                return 0
            else:
                return minleng

                   
        
                   
        
