class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            arr.append(sum1)
        return arr
        # arr=[]
        # for i in range(1,len(nums)+1):
        #     arr.append(sum(nums[:i]))   
        # return arr
