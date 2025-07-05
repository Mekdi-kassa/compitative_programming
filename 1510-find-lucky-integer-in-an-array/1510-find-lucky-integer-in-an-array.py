class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        x = 0
        for num in count:
            if num == count[num]:
                x = max(x , num)
        if x > 0:
            return x
        return -1