class Solution(object):
    def fib(self, n):
        # memo = {}
        # def fib1(i):
        #     if i == 0:
        #         return 0
        #     elif i == 1:
        #         return 1
        #     if i not in memo:
        #         memo[i] = self.fib(i-1)+self.fib(i-2)
        #     return memo[i]
        # return fib1(n)


        # using bottom_up
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev = 1
        prevp = 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        ans = 0
        for i in range(2 ,n + 1):
            ans = prev + prevp
            prevp = prev
            prev = ans
        return ans