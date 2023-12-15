class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.zero = set( [i for i in range(size)] )
        self.one_set = set()

    def fix(self, idx: int) -> None:
        self.one_set.add(idx)
        self.zero.discard(idx)

    def unfix(self, idx: int) -> None:
        self.one_set.discard(idx)
        self.zero.add(idx)

    def flip(self) -> None: #o(n) 105 fix this to 0(1) // fixed // old code deleted
        temp = self.one_set
        self.one_set = self.zero 
        self.zero = temp
        # optimise this
        # reverse 1's and zeros       

        
    def all(self) -> bool:
        return len(self.one_set) == self.size

    def one(self) -> bool:
        return  len(self.one_set) > 0

    def count(self) -> int:
        return len(self.one_set)

    def toString(self) -> str:
        s = []
        for i in range(self.size):
            if i in self.one_set:
                s.append("1")
            elif i in self.zero:
                s.append("0")

        return ''.join(s)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()