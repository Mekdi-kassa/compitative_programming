class TrieNode:
# Trie node class
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            ind = ord(w) - ord('a') 
            # curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node , ind):
            if ind == len(word):
                return node.is_end

            char = word[ind]

            if char != ".":
                i = ord(char) - ord('a')
                if i not in node.children:
                    return False
                return dfs(node.children[i],ind + 1)

            for child in node.children:
                if dfs(node.children[child] , ind + 1):
                    return True
            return False
        return dfs(self.root , 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)