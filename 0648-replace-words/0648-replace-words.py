from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort dictionary by length to find shortest roots first
        dictionary.sort(key=len)
        arr = list(map(str, sentence.split()))
        
        # Insert dictionary words into trie, not sentence words
        def insert(word):
            curr = self.root
            for w in word:
                idx = ord(w) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.is_end = True
        
        # Insert all dictionary words
        for word in dictionary:
            insert(word)
        ans = ""
        def search(word):
            ans = ""
            curr = self.root
            for w in word:
                ind = ord(w) - ord('a') 
                if (curr.children[ind] == None) and not curr.is_end:
                    return word  
                ans += w
                curr = curr.children[ind]
                if curr.is_end:
                    return ans  
            return word 
                
            

        
        for word in arr:
            x = search(word) + " "
            ans += x
        return ans[:-1]
        
