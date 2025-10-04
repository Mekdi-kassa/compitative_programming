class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr=float('-inf')
        left = 0
        right = len(height)-1
        while left< right:
            min_hight=min(height[left],height[right])
            width = right - left 
            arr=max(min_hight*width,arr)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return arr