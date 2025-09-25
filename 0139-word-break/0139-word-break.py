class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}
        
        def dp(i, current):
            if i == n:
                return current in wordSet or current == ""
            
            key = (i, current)  # Proper memo key
            if key in memo:
                return memo[key]
            
            # Option 1: Continue building current word
            continue_word = dp(i + 1, current + s[i])
            
            # Option 2: If current is valid word, start new word
            start_new = False
            if current in wordSet:
                start_new = dp(i + 1, s[i])
            
            memo[key] = continue_word or start_new
            return memo[key]
        
        return dp(0, "")