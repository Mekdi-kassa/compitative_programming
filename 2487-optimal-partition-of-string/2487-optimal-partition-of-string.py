class Solution:
    def partitionString(self, s: str) -> int:
        strs = ""
        count = 0
        for char in s:
            if char not in strs:
                strs += char
            else:
                strs = ""
                strs += char
                count += 1
        count += 1
        return count