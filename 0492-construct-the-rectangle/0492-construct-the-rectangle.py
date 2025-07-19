class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        arr = []
        for i in range(1, int(area**0.5) + 1):  
            if area % i == 0:
                arr.append((i, area//i, abs(i - area//i)))
        
        
        arr.sort(key=lambda x: x[2])
        return [arr[0][1], arr[0][0]]  