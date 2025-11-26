class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k: int) -> bool:
            removed = set(removable[:k])
            i = 0
            for j, c in enumerate(s):
                if j in removed:
                    continue
                if c == p[i]:
                    i += 1
                    if i == len(p):
                        return True
            return i == len(p)
        
        left, right = 0, len(removable)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if is_subsequence(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans