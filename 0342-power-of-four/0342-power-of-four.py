class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        flag = False
        i = 0
        j = 0
        while i == 0:
            y = 4 ** j
            if y == n:
                i = 1
                flag = True
            elif y > n:
                i = 1
            j += 1
        if flag :
            return True
        return False