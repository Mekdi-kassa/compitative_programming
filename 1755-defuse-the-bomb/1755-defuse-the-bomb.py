class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        # Create extended array for circular access
        extended = code + code
        
        result = []
        for i in range(n):
            if k > 0:
                # Sum next k elements
                total = sum(extended[i+1:i+1+k])
            else:
                # Sum previous k elements (k is negative)
                total = sum(extended[i+n+k:i+n])
            result.append(total)
        
        return result