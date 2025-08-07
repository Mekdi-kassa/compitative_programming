class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            #sliding window
            c = Counter(s1)
            arr = defaultdict(int)
            if len(s2) < len(s1):
                return False
            for i in range(len(s1)-1):
                arr[s2[i]] += 1
            j = 0
            for i in range(len(s1)-1 , len(s2)):
                arr[s2[i]] += 1
                if arr == c:
                    return True
                arr[s2[j]] -= 1
                if arr[s2[j]] == 0:
                    del arr[s2[j]]
                j += 1
            return False
                


        