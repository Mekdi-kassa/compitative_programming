class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        sum1=0
        for i in range(left,right+1):
            sum1+=self.nums[i]
        return sum1


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)