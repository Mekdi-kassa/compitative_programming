class Solution(object):
    def longestCommonPrefix(self, strs):
        shortestStr = strs[0]
        for i in strs:
            if len(i) < len(strs[0]):
                shortestStr = i
        for i in range(len(shortestStr)):
            currentChar = shortestStr[i]
            for word in strs:
                if(word[i]) != currentChar:
                    return shortestStr[:i]
        return shortestStr