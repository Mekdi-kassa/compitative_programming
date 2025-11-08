class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opr=set(['/','*','+','-'])
        for i in range(len(tokens)):
            if tokens[i] in opr:
                num1=stack.pop()
                num2=stack.pop()
                if tokens[i] == '/':
                    ans=int(num2/num1)
                    stack.append(ans)
                elif tokens[i] == '*':
                    ans=num1*num2
                    stack.append(ans)
                elif tokens[i] == '+':
                    ans=num1+num2
                    stack.append(ans)
                elif tokens[i] == '-':
                    ans=num2-num1
                    stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        return  stack[-1]