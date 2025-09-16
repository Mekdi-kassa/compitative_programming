class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        left  = 0
        for word in words:
            n = len(word)
            if left  == len(s):
                break
            if left + n > len(s):
                return False
            elif s[left:left + n] != word:
                return False
            left += n
        if left == len(s):

            return True
        else:
            return False