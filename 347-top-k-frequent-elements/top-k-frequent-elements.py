class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using heap
        count = Counter(nums)
        heap = []
        for key,val in count.items():
            heapq.heappush(heap,(-val,key))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans