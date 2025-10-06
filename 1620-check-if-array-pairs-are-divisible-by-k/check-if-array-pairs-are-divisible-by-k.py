class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dict1 = defaultdict(int)
        for i in range(len(arr)):
            rem = arr[i] % k
            if rem >= 0:
                dict1[rem] += 1
            else:
                dict1[rem + k] += 1
        for key , val in dict1.items():
            if key == 0:
                if val % 2 != 0:
                    return False
            elif dict1[key] != dict1[k - key]:
                return False
        return True

           
