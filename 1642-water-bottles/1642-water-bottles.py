class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        x=numBottles-1
        y=numExchange-1
        sum=x/y
        return numBottles+sum
    


        