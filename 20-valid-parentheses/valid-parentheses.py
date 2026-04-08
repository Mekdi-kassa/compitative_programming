class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        val={')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in val:
                if res and val[s[i]]==res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])
        return not res