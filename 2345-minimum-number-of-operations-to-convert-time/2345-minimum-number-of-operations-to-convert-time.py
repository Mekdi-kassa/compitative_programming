class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        final = int(correct[:2]) * 60
        curr = int(current[:2]) * 60 
        min_final = int(correct[3:])
        min_curr = int(current[3:])
        count = 0
        min1 = (final + min_final) - (curr + min_curr)
        if min1 >= 60:
            m = min1 // 60
            min1 = min1 % 60
            count += m
        if min1 >= 15:
            m = min1 // 15
            min1 = min1 % 15
            count += m
        
        if min1 >= 5:
            m = min1 // 5
            min1 = min1 % 5
            count += m
        
        if min1 >= 1:
            m = min1 // 1
            min1 = min1 % 1
            count += m 
        
        return count 