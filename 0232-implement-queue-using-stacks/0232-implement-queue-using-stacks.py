class MyQueue:

    def __init__(self):
        self.que = deque([])
    def push(self, x: int) -> None:
        self.que.append(x)
    def pop(self) -> int:
        y = self.que.popleft()
        return y
    def peek(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        if len(self.que) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()