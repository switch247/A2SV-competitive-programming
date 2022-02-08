class MyQueue:

    def __init__(self):
        self.stalk1=[]
        self.stalk2=[]

    def push(self, x: int) -> None:
        self.stalk1.append(x)
        
    def pop(self) -> int:
        return self.stalk1.pop(0)
        
    def peek(self) -> int:
        return self.stalk1[0]

    def empty(self) -> bool:
        return False if self.stalk1 else True 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
