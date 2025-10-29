class Solution:
    def countVowels(self, word: str) -> int:
        
        set1 = set(['a' , 'e' , 'i' , 'o' , 'u' ])
        total = 0
        n = len(word)
        for i in range(n):
            if word[i] in set1:
                total += (i + 1) * (n - i)
        return total