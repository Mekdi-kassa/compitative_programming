class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first():
            low = 0
            high = len(nums)-1
            first=-1
            while low <= high:
                mid=(low + high)//2
                if nums[mid] == target:
                    first=mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return first

        def last():
            low = 0
            high = len(nums)-1
            last=-1
            while low <= high:
                mid=(low + high)//2
                if nums[mid] == target:
                    last=mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return last

        return [first(),last()]
        # print(last())
        # print(first())
        