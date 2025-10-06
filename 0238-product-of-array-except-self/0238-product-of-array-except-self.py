class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro=1
        right_pro=1
        left_arr=[0]*len(nums)
        right_arr=[0]*len(nums)
        j=-1
        for i in range(len(nums)):
            left_arr[i]=left_pro
            right_arr[j]=right_pro
            right_pro*=nums[j]
            left_pro*=nums[i]
            j-=1
        return [l*r for l,r in zip(left_arr,right_arr)]