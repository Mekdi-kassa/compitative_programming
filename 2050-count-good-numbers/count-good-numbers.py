class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 1:
            return 5
        elif n % 2 == 0:
            even = pow(5 , n//2 , mod)
            odd = pow(4 , n//2 ,mod)
            res = ((even) * (odd)) % mod
        else:
            even = pow(5 , (n//2) + 1 , mod)
            odd = pow(4 , n//2 ,mod)
            res = ((even) * (odd)) % mod
        return res