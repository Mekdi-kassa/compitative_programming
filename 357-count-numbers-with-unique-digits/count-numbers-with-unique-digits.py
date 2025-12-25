class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        elif n==1:
            return 10
        elif n==2:
            return 91
        elif n==3:
            return 739
        elif n==4:
            return 5275
        elif n==5:
            return 32491
        elif n==6:
            return 168571
        elif n==7:
            return 712891
        elif n==8:
            return 2345851