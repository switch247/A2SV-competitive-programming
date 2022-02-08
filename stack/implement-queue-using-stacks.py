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
  '''class MyQueue:

    def __init__(self):
        # Initializing two Stack. stack1 and stack2
        self.stack1 = []
        self.stack2 = [] # fill this by poping from stalk1 to stack2[-1]==stlk1[0]

    def push(self, x: int) -> None:
        # Appending the value to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        """Since in stack we can only pop element from last. We first pop all the element from stack1 and append it to stack2. After that we pop the last element from stack2"""
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # Same expaination as pop
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check the length of both the stack and return the answer.
        return len(self.stack1) == 0 and len(self.stack2) == 0
  
  
  '''
