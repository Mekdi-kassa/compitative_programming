import numpy as np
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = np.zeros(len(s), dtype=int)
        for start,end,direction in shifts:
            if direction==0:
                prefix_sum[start:end+1]-=1   
            else:
                prefix_sum[start:end+1]+=1
        print(prefix_sum)    
        arr=[]
        shift=0
        for i in range(len(s)):
            x=chr(((ord(s[i])- ord('a') + prefix_sum[i] )%26)+ord('a'))
            arr.append(x)
        return "".join(arr)


