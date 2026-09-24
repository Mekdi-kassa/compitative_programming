class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        right = 0 
        n = len(fruits)
        max1 = 0
        dict1 = defaultdict(int)
        while right < n:
            dict1[fruits[right]] += 1
            while len(dict1) > 2:
                dict1[fruits[left]] -= 1
                if dict1[fruits[left]] < 1:
                    dict1.pop(fruits[left])
                left += 1
            max1 = max(max1 ,(right - left + 1))
            right += 1
        return max1
            
