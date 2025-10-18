class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=1
        arr=[]
        while i<=len(s):
            for j in range(len(s)-i+1):
                sub=s[j:j+i]
                if sub==sub[::-1]:
                    arr.append(sub)
            i+=1
        if len(arr)>0:
            return arr[-1]
        else:
            return ""
        