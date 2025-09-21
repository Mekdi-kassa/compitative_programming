class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my=set()
        for start, end in ranges:
            for num in range(start, end + 1):
                my.add(num)
        for i in range(left,right+1):
            if i not in my:
                return False
        return True

