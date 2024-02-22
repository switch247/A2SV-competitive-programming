class MyStack:
    from collections import deque

    def __init__(self):
        self.d=deque()
        

    def push(self, x: int) -> None:
        return self.d.append(x)
        

    def pop(self) -> int:
        return self.d.pop()

    def top(self) -> int:
        return list(self.d)[-1]

    def empty(self) -> bool:
        return len((self.d)) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()