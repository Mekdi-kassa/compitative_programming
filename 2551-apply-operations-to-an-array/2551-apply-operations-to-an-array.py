class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                mul = nums[i] * 2
                nums[i] = mul
                nums[i + 1] = 0
        arr = []
        count = 0
        for i in range(n):
            if nums[i] != 0:
                arr.append(nums[i])
            else:
                count += 1
        for i in range(count):
            arr.append(0)
        return arr
        

