class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = {}
        def dp(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i > n:
                return
            
            if i not in memo:
                way = dp(i + 1)
                if i + 2 <= n and 10 <= int(s[i:i + 2]) <=26 :
                    way += dp(i + 2)
                memo[i] = way
            return memo[i]
        if s[0] == "0":
            return 0
        return dp(0)

