class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c ** 0.5) + 1):
            a = i ** 2
            b = c - a
            b_sqr = int(b ** 0.5)
            if b_sqr ** 2 == b:
                return True
        return False
