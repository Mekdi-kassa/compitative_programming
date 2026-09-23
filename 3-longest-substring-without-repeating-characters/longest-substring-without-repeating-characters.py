class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = defaultdict(int)
        j = 0
        n = len(s)
        max1 = 0
        for i in range(n):
            dict1[s[i]] += 1
            while dict1[s[i]] > 1:
                dict1[s[j]] -= 1
                j += 1
            max1 = max(max1 , (i - j + 1))
        return max1