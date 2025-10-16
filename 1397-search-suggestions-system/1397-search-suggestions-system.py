class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def insert(word):
            curr = self.root
            for char in word:
                ind = ord(char) - ord('a')
                # curr.children[ind] = TrieNode()
                curr = curr.children[ind]
            curr.is_end = True
        
        for product in products:
            insert(product)
        def search(word):
            ans = []
            curr = self.root
            for w in word:
                ind = ord(w) - ord('a')
                if curr.children[ind] == None:
                    return []
                curr = curr.children[ind]
            res = []
            dfs(curr , word , res)
            return res
        def dfs(curr , word , res):
            if curr.is_end:
                res.append(word)
            for ind , child in curr.children.items():
                ch = chr( ind + ord('a'))
                dfs(child , word + ch , res)
        n = len(searchWord)
        ans = ""
        res = []
        for i in range(n):
            ans += searchWord[i]
            a = search(ans)
            a.sort()
            if len(a) >= 3:
                res.append(a[:3])
            else:
                res.append(a)
        return res

