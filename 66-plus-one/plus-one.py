class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs = "".join(map(str,digits))
        num1 = str(int(strs) + 1)
        return list(map(int,num1.strip()))