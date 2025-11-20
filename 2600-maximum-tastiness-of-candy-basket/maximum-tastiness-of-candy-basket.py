class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        def can_achieve(t: int) -> bool:
            count = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= t:
                    count += 1
                    last = p
                    if count == k:
                        return True
            return False
        
        left, right = 0, price[-1] - price[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans