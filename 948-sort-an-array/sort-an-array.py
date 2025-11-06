class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(right_arr ,left_arr):
            left = 0 
            right = 0
            ans = []
            while left < len(left_arr) and right < len(right_arr) :
                if left_arr[left] < right_arr[right]:
                    ans.append(left_arr[left])
                    left += 1
                else:
                    ans.append(right_arr[right])
                    right += 1
            while left < len(left_arr):
                ans.append(left_arr[left])
                left += 1
            while right < len(right_arr):
                ans.append(right_arr[right])
                right += 1
            return ans
        def merge(arr):
            if len(arr) == 1:
                return arr
            n = len(arr)// 2
            left_arr =merge(arr[:n])
            
            right_arr = merge(arr[n:])

            return merge_sort(right_arr , left_arr)
        return merge(nums)