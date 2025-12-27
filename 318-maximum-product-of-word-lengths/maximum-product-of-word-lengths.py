class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        max1 = 0
        mask = [0] * n
        for i in range(n):
            for ch in words[i]:
                mask[i] |= 1 << (ord(ch) - ord("a")) 
        
        for i in range(n):
            for j in range(i + 1, n):
                if mask[i] & mask[j] == 0:
                    max1 = max(max1 , (len(words[i])*len(words[j])))
        return max1