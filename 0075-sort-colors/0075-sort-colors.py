class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict1 ={i:0 for i in range(3)}
        for num in nums:
            dict1[num] += 1
        
        j = 0
        for i in dict1:
            for k in range(dict1[i]):
                nums[j] = i
                j += 1
        
