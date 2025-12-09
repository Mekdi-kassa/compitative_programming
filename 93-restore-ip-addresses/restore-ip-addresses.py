class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def back(i, dot, strs):
            if dot == 4 and i == len(s):
                res.append(strs[:-1])  
                return 
            if dot > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j + 1]
                if int(segment) < 256 and (i == j or s[i] != "0"):
                    back(j + 1, dot + 1, strs + segment + ".")
        
        back(0, 0, "")
        return res