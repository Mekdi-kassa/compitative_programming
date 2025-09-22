class Solution(object):
    def fib(self, n):
        memo = {}
        def fib1(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            if i not in memo:
                memo[i] = self.fib(i-1)+self.fib(i-2)
            return memo[i]
        return fib1(n)