class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        arr = deque([])
        cost = 0
        ans = []
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            arr.append(s[i])
            while cost > maxCost:
                x = abs(ord(s[left]) - ord(t[left]))
                cost -= x
                arr.popleft()
                left += 1
            ans.append(len(arr))
        return max(ans)

