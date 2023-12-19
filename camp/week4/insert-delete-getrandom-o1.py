class RandomizedSet:

    def __init__(self):
        self.numdict = {} # val:index (index = len-1)
        self.numlist = [] # value: the number
        return


    def insert(self, val: int) -> bool:
        if val in self.numdict:
            return False
        self.numlist.append(val)
        self.numdict[val] = len(self.numlist)-1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.numdict:
            return False
        oldpos = self.numdict[val]

        self.numdict.pop(val)
        
        if oldpos == len(self.numlist)-1:
            self.numlist.pop()
        else:
            self.numdict[ self.numlist[-1] ] = oldpos
            self.numlist[oldpos] , self.numlist[-1] = self.numlist[-1], self.numlist[oldpos]

            self.numlist.pop()
            
        return True
        

    def getRandom(self) -> int:
        # return random.choice(self.numlist)
        return self.numlist[int(random.random() * len(self.numlist))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()