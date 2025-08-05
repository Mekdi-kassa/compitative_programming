class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        left = 0
        n = len(s)
        max1 = 0
        for i in range(n):
            while s[i] in set1:
                set1.remove(s[left])
                left += 1
            set1.add(s[i])
            max1 = max(max1 , i - left + 1)
        return max1
                