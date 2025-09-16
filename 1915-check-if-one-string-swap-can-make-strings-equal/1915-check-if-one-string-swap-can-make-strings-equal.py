class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count = 0
        set1 = set()
        if set(s1) != set(s2):
            return False
        else:
            for i in range(n):
                if s1[i] != s2[i]:
                    count += 1
                    set1.add(s1[i])
                    set1.add(s2[i])
                
                if count > 2:
                    return False
            if (count == 0 or count == 2) and (len(set1) == 2 or len(set1) == 0):
                return True
            return False
            