from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for word in strs:
            x = "".join(sorted(word))
            dict1[x].append(word)
        arr = []
        for val in dict1:
            arr.append(dict1[val])
        return arr
