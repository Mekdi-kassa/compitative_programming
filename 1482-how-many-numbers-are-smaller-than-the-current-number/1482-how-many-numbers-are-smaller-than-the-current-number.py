class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        mat = [[nums[i]  , i] for i in range(len(nums))]
        mat.sort(key=lambda x: x[0])
        prev = float('inf')
        j = float('inf')
        for i in range(len(mat)):
            key , value = mat[i]
            if key != prev:
                ans[value] = i
                prev = key
                j = i
            else:
                ans[value] = j

        print(mat)
        return ans