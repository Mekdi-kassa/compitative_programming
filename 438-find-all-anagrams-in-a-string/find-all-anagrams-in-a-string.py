class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        dict1 = defaultdict(int)
        dict2 = Counter(p)
        if len(s) < len(p):
            return []
        for i in range(m -1):
            dict1[s[i]] += 1
        l = 0
        ans = []
        for j in range(m-1  , n):
            dict1[s[j]] += 1
            if dict1 == dict2:
                ans.append(l)
            dict1[s[l]] -= 1
            if dict1[s[l]] == 0:
                dict1.pop(s[l])
            l += 1

        return ans