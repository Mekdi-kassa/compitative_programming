class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [[nums[i],i] for i in range(len(nums))]
        arr.sort(key=lambda x: x[0])
        ans = [0]*len(nums)
        for i in range(len(arr)):
            if i > 0 and arr[i][0] == arr[i - 1][0]:
                ans[arr[i][1]] = ans[arr[i-1][1]]
            else:
                ans[arr[i][1]] = i
                

        return ans

