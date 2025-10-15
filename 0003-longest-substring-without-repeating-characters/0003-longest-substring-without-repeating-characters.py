class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        max_len = 0
        dict1 = defaultdict(int)
        for r in range(n):
            dict1[s[r]] += 1
            while dict1[s[r]] > 1:
                dict1[s[l]] -= 1
                l +=1 
            max_len = max(max_len , (r - l + 1)) 
        return max_len
