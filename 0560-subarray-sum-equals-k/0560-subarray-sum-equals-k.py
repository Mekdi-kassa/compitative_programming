class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1=defaultdict(int)
        dict1[0]+=1
        sum1=0
        count=0
        for i in range(len(nums)):
            sum1+=nums[i]
            pre=(sum1-k)
            count+=dict1[pre]
            dict1[sum1]+=1
        return count