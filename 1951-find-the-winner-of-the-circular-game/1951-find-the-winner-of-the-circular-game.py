class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # count=0
        # all_element_sum=n*(n+1)//2
        # remove_list=set()
        # i=1
        # while i<=n:
        #     count+=1
        #     if len(remove_list)==n-1:
        #         break
        #     if count==k and i not in remove_list:
        #         remove_list.add(i)
        #         count=0
        #     elif i in remove_list:
        #         count-=1
        #     if i==n:
        #         i=0
        #     i+=1
        # sum1=sum(list(remove_list))
        # return all_element_sum-sum1
        que = deque([])
        for i in range(1 , n + 1):
            que.append(i)
        while len(que) > 1:
            for i in range(k-1):
                val = que.popleft()
                que.append(val)
            que.popleft()
        return que[0]




           
            