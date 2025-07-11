class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        set1 = set()
        for i in range(1,len(matrix) + 1):
            set1.add(i)
        def checkrow(set1):
            for row in matrix:
                if set(row) != set1:
                    return False
            return True
        def checkcol(set1):
            for i in range(len(matrix)):
                set2 = set()
                for j in range(len(matrix[0])):
                    set2.add(matrix[j][i])
                if set2 != set1:
                    return False
            return True

        return checkrow(set1) and checkcol(set1)
