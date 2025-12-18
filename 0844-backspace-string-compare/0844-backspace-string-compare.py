class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        for i in range(len(s)):
            if s[i]=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
        stack2=[]
        for i in range(len(t)):
            if t[i]=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[i])
        return stack1==stack2