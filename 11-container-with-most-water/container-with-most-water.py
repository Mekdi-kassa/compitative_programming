class Solution:
    def maxArea(self, height: list[int]) -> int:

        n = len(height)
        left = 0
        right = n - 1
        max1 = 0
        while left < right:
            cal = min(height[left] , height[right])
            max1 = max(max1 , (cal * (right - left)))
            if cal == height[left]:
                left += 1
            else:
                right -= 1
        return max1
