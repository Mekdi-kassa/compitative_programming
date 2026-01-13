class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        x = right & left
        diff = right - left
        ans = 0
        for i in range(31):
            if x & (1 << i):
                print(i)
                if diff < (2 ** i):
                    ans +=(2 ** i) 
        return ans



                