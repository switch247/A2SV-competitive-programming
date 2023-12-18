class ATM:

    def __init__(self):
        # self.balance = 0
        self.denominators = [20, 50, 100, 200, 500]
        self.notes = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        self.notes = [a + b for a, b in zip(self.notes, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        # the hard part
        take = [0] * 5
        for i in range(4, -1, -1):
            take[i] = min(self.notes[i], amount // self.denominators[i])
            amount -= take[i] * self.denominators[i]
        if amount == 0:
            self.notes = [a - b for a, b in zip(self.notes, take)]
        return [-1] if amount else take




# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)