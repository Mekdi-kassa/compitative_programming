class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {"2":["a","b","c"], "3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if len(digits) == 0:
            return []
        def backtrack(ind,ans,store):
            if ind == len(digits):
                ans.append("".join(store))
                return 
            for char in dict1[digits[ind]]:
                store.append(char)
                backtrack(ind + 1 , ans, store)
                store.pop()
        ans = []
        backtrack(0,ans,[])
        return ans

