class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def parenthesis(opencount,closecount,store):
            if opencount == closecount == n:
                res.append("".join(store))
                return 

            if opencount < n:
                store.append("(")
                parenthesis(opencount + 1,closecount ,store)
                store.pop()

            if closecount < opencount:
                store.append(")")
                parenthesis(opencount ,closecount + 1 ,store)
                store.pop()

       
        parenthesis(0 ,0 ,[])
        return res