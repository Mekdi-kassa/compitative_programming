class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        set1=set()
        set2=set(nums)
        arr=[0]*2
        for i in range(1,len(nums)+1):
            set1.add(i)
        for i in set1:
            if count[i]==2:
                arr[0]=i
            elif i not in set2:
                arr[-1]=i
        return arr