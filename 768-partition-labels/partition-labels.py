class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        set1 = set()
        count1 = Counter(s)


        res = []
        
        start = 0
        for i in range(len(s)):
            count1[s[i]] -= 1
            if s[i] not in set1 and count1[s[i]] != 0:
                set1.add(s[i])
            elif count1[s[i]] == 0 and s[i] not in set1 and len(set1) == 0:
                res.append(i - start + 1)
                start = i + 1
            elif count1[s[i]] == 0 and s[i] in set1:
                set1.remove(s[i])
                if len(set1) == 0:
                    res.append(i - start + 1)
                    start = i + 1

        return res
        
            
            