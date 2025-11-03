class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=[]
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            result=chr(rem+ord('A'))
            res.append(result)
            columnNumber//=26
        return "".join(reversed(res))
        