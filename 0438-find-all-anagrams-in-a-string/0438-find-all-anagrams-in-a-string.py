from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count=Counter(p)
        arr=[]
        n=len(p)
        dict1 = defaultdict(int)
        if len(s)<len(p):
            return []
        for i in range(len(p)-1):
            dict1[s[i]]+=1
        j=0
        for i in range(len(p)-1,len(s)):
            dict1[s[i]]+=1
            if dict1==count:
                arr.append(j)
            dict1[s[j]]-=1
            if dict1[s[j]]==0:
                dict1.pop(s[j])
            j+=1
        return arr
            
        