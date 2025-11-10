class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ones = {}
        for i in range(len(bank)):
            ones[i] = bank[i].count("1")

        ans = 0
        for i in range(len(bank)):
            curr_count = ones[i]
            for j in range(i + 1, len(bank)):
                if ones[j] != 0:
                    ans += (curr_count * ones[j])
                    break

        return ans
