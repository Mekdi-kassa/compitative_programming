class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)
        idx = 0
        offers_by_end = [[] for _ in range(n)]
        for s, e, g in offers:
            offers_by_end[e].append((s, g))
        for i in range(n):
            dp[i+1] = max(dp[i+1], dp[i])
            for s, g in offers_by_end[i]:
                dp[i+1] = max(dp[i+1], dp[s] + g)
        return dp[n]