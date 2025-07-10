class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
        sum1 = 0
        for num in count:
            for i in range(len(count[num])):
                for j in range(i + 1 , len(count[num])):
                    if (count[num][i] * count[num][j]) % k == 0:
                        sum1 += 1
        return sum1
