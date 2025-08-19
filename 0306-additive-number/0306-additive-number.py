class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def numberadd(i,ans,store):
            if len(store) >= 3 and store[-1]!=store[-2] + store[-3]: 
                return False
                

            if i == len(num):
                return len(store) >= 3
            
            for j in range(i+1,len(num)+1):
                part=num[i:j]
                if len(part) > 1 and part[0]=='0':
                    continue

                store.append(int(part))
                if numberadd(j,ans,store):
                    return True
                
                store.pop()
            return False
            # if str(int(num[i])) == num[i] and num[i]!='0':
            #     store.append(int(num[i]))
            #     numberadd(i+1,ans,store)
            #     store.pop()
            #     numberadd(i+1,ans,store)
            

        ans=[]
        return numberadd(0,ans,[])
        