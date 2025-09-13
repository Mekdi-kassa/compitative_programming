class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowel = {'a','e','i','o','u'}
        maxv = 0
        maxc = 0
        for chars in count:
            if chars in vowel:
                maxv = max(maxv,count[chars])
            else:
                maxc = max(maxc,count[chars])
        return maxc + maxv
