class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        found=False
        mid=0
        while not found and high >= low:
            mid=(high + low)//2
            if nums[mid] == target:
                found=True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if found:
            return mid
        else:
            return -1