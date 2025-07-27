class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 = Counter(arr1)
        ans = []
        last = []
        for num in arr2:
            if num in arr2 and num not in ans:
                for i in range(dict1[num]):
                    ans.append(num)
        for i in arr1:
            if i not in ans:
                last.append(i)
        last.sort()
        return ans + last


            

        