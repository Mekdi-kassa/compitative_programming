from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  
            return False

        lowr = 0
        highr = len(matrix) - 1  
        lowc = 0
        highc = len(matrix[0]) - 1  

        while lowr <= highr and lowc <= highc:
            mid1 = (lowr + highr) // 2
            mid2 = (lowc + highc) // 2
            
            if matrix[mid1][mid2] == target:
                return True
            elif matrix[mid1][mid2] > target:
                highc = mid2 - 1 
                if highc < 0: 
                    highr = mid1 - 1
                    highc = len(matrix[0]) - 1  
            else:
                lowc = mid2 + 1  
                if lowc >= len(matrix[0]): 
                    lowr = mid1 + 1
                    lowc = 0  

        return False