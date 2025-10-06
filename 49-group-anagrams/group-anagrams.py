class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        ans = []
        for word in strs:
            s = list(map(str,word.strip()))
            s.sort()
            w = "".join(s)
            dict1[w].append(word)
        for val in dict1:
            ans.append(dict1[val])
        return ans