class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        dict1 = defaultdict(int)
        n = len(s)
        total = 0
        while right < n:
            dict1[s[right]] += 1
            while (right - left + 1) - max(dict1.values()) > k:
                dict1[s[left]] -= 1
                if dict1[s[left]] < 1:
                    dict1.pop(s[left])
                left += 1
            total = max(total , (right - left + 1))
            right += 1
        return total

            
