class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        sum1=0
        for key, val in count.items():
            if key==0:
                sum1+=val
            else:
                sum1+=((val+key)//(key+1)*(key+1))
        return sum1