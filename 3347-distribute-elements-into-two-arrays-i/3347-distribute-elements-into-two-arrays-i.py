class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])

        for i in range(2,n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        result = arr1 + arr2
        return result
