class Solution(object):
    def reverse(self, x):
        if x>=0:
            m=int(str(x)[::-1])
            if m>=-2**31 and m<=2**31-1:
                return m
            else:
                return 0
        else:
            m=-int(str(x)[1:][::-1])
            if m>=-2**31 and m<=2**31-1:
                return m
            else:
                return 0
            
        
            