class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()  
        prices = []
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            prices.append(price)
            max_beauty.append(current_max)
        
        answer = []
        for q in queries:
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:
                answer.append(max_beauty[idx])
            else:
                answer.append(0)
        return answer