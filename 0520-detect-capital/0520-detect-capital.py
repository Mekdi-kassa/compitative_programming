class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].upper() in word[0]:
            x=word[1:]
            if x.lower() in x:
                return True
            elif x.upper() in x:
                return True
            else:
                return False
        elif word[0].lower() in word[0]:
            x=word[1:]
            if x.lower() in x:
                return True
            else:
                return False