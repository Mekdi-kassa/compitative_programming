class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum=[0]*(len(s)+1)
        for start,end,direction in shifts:
            if direction==0:
                prefix_sum[start]-=1
                prefix_sum[end+1]+=1
            else:
                prefix_sum[start]+=1
                prefix_sum[end+1]-=1
        arr=[]
        shift=0
        for i in range(len(s)):
            shift += prefix_sum[i] 
            x=chr(((ord(s[i])- ord('a') + shift )%26)+ord('a'))
            arr.append(x)
        return "".join(arr)



