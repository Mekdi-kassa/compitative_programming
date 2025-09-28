class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if Counter(s) == Counter(t):
        #     return True
        # return False
        # the above is o(n) space o(n) time

        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        for char in t:
            freq[ord(char) - ord('a')] -= 1
            if freq[ord(char) - ord('a')] < 0:
                return False
        return True