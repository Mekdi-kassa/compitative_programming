class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr  = list(map(str , text.split()))
        set1 = set(brokenLetters)
        ans = 0
        for word in arr:
            if not set(word) & set1:
                ans += 1
        return ans
