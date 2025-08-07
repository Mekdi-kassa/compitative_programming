from collections import defaultdict, deque
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        arr = defaultdict(int)
        arr1 = deque()
        ans = []
        left = 0
        for i in range(len(fruits)):
            arr[fruits[i]] += 1
            arr1.append(fruits[i])
            if len(arr) == 2:
                ans.append(len(arr1))
    
            while len(arr) == 3:
                arr[fruits[left]] -= 1
                arr1.popleft()
                if arr[fruits[left]] == 0:
                    del arr[fruits[left]] 
                left += 1

            
        ans.append(len(arr1))
        return max(ans)