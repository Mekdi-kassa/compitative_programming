import math

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        
        for i in nums:
            divisors = [] 
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    divisors.append(j)  # j is a divisor
                    if j != i // j:  # Avoid adding the square root twice
                        divisors.append(i // j)
                if len(divisors) > 4:  # If more than 4 divisors, stop checking
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total


        