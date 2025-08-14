class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        out=""
        arr=[]
        for i in range(len(num)-2):
            out=""
            if int(num[i])==int(num[i+1])==int(num[i+2]):
                    out+=num[i:i+3]
                    arr.append(int(out))
        if len(arr)>0 and str(max(arr))=="0": 
            return "000"
        elif len(arr)>0 and str(max(arr))!="0":
            return str(max(arr))
        else:
            return ""