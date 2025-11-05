class NumberContainers:

    def __init__(self):
        self.arr = defaultdict(list)
        self.arr1 = defaultdict(int)
    def change(self, index: int, number: int) -> None:
        if index in self.arr1:
            old_num = self.arr1[index]
        self.arr1[index] = number
        heapq.heappush(self.arr[number] , index)

    def find(self, number: int) -> int:
        if number not in self.arr:
            return -1
        
        heap = self.arr[number]
        while heap and self.arr1[heap[0]] != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1


# Your NumberContainers object will bez instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)