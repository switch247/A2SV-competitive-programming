class Robot:

    def __init__(self, width: int, height: int):
        self.width = width -1
        self.height = height -1
        self.location = [0,0]
        self.dir = ["East","North","West","South"]
        self.dirc = 0 #we start facing east
        
    def step(self, num: int) -> None:
        # we might loop around acount for that
        num = num%((self.width + self.height)*2)
        if num == 0 :
            if self.location == [0,0]:
                self.dirc = 3
            elif self.location == [self.width,0]:
                self.dirc = 0
            elif self.location ==[self.width,self.height] :
                self.dirc = 1
            elif self.dirc == [0,self.height]:
                self.dirc = 2

        
        while num > 0:
            if self.dirc == 0:
                # go east as far as you can
                num = self.location[0] + num - self.width
                if num <= 0:
                    self.location[0] = self.width + num
                else:
                    self.dirc = (self.dirc + 1)%4
                    self.location[0] = self.width
                
            elif self.dirc == 1:
                # north
                num = self.location[1] + num - self.height
                if num <= 0:
                    self.location[1] = self.height + num
                else:
                    self.dirc = (self.dirc + 1)%4
                    self.location[1] = self.height
            
            elif self.dirc == 2:
                # west
                num = self.location[0] - num

                if num >=0:
                    self.location[0] = num
                    num = 0
                else:
                    self.dirc = (self.dirc + 1)%4
                    self.location[0] = 0
                    num = abs(num)

            elif self.dirc == 3:
                # s
                num = self.location[1] - num

                if num >=0:
                    self.location[1] = num
                    num = 0
                else:
                    self.dirc = (self.dirc + 1)%4
                    self.location[1] = 0
                    num = abs(num)

    def getPos(self) -> List[int]:
        
        return self.location

    def getDir(self) -> str:
        return self.dir[self.dirc]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()