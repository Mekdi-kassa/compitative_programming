class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        randsum=0
        for i in range(0,len(s)-1):
            if my_dict[s[i+1]]>my_dict[s[i]]:
                randsum-=my_dict[s[i]]
            else:
                randsum+=my_dict[s[i]]
        return randsum+my_dict[s[-1]]
