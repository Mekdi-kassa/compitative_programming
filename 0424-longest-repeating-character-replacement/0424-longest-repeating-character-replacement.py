from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])  # Track most frequent char in the window
            
            # Shrink the window if replacements needed exceed k
            while (right - left + 1 - max_freq) > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result