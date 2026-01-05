class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        # self.children =defaultdict(lambda:None)


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if  curr.children[(ord(w) - ord('a'))] == None:
                curr.children[(ord(w) - ord('a'))] = TrieNode()
            curr = curr.children[(ord(w) - ord('a'))]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if curr.children[(ord(w) - ord('a'))] == None:
                return False
            curr = curr.children[(ord(w) - ord('a'))]
        if curr.is_end:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for w in prefix:
            if curr.children[(ord(w) - ord('a'))] == None:
                return False
            curr = curr.children[(ord(w) - ord('a'))]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)