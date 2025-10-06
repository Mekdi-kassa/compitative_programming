class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # dict1 = defaultdict(int)
        # for i in range(len(arr)):
        #     rem = arr[i] % k
        #     if rem >= 0:
        #         dict1[rem] += 1
        #     else:
        #         dict1[rem + k] += 1
        # for key , val in dict1.items():
        #     if key == 0:
        #         if val % 2 != 0:
        #             return False
        #     elif dict1[key] != dict1[k - key]:
        #         return False
        # return True
        dict1 = [0] * k
        for num in arr:
            dict1[num % k] += 1
        if k % 2 == 0 and (dict1[k//2] %2 == 1 or dict1[0] % 2== 1):
            return False
        
        for i in range(1 , k):
            if dict1[i] != dict1[(-i) % k]:
                return False
        return True

           
