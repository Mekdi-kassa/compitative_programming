class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for k in range(4):  
            t = n - k * (limit + 1)
            if t < 0:
                continue

            ways = (t + 2) * (t + 1) // 2

            if k == 0:
                coeff = 1
            elif k == 1:
                coeff = 3
            elif k == 2:
                coeff = 3
            else:
                coeff = 1

            if k % 2 == 0:
                total += coeff * ways
            else:
                total -= coeff * ways

        return total
