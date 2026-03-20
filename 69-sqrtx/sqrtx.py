class Solution:
    def mySqrt(self, x: int) -> int:
        # squareroot=0
        # n=0
        # j=x//2
        # if x == 1:
        #     return 1
        # while n*n<=x and n<=j:
        #     squareroot=n
        #     n+=1
        # return squareroot

        high=x
        low=0
        ele=0
        while high >= low:
            mid=(low+high)//2
            if  mid*mid == x:
                return mid
            elif mid*mid > x:
                high=mid-1
            else:
                low=mid+1
        return high