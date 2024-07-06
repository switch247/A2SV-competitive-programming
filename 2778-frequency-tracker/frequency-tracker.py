class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.freqSet = {}

    def add(self, number: int) -> None:
        if number in self.freq:
            old_freq = self.freq[number]
            self.freq[number] += 1
            self.freqSet[old_freq].remove(number)
            if self.freq[number] not in self.freqSet:
                self.freqSet[self.freq[number]] = set()
            self.freqSet[self.freq[number]].add(number)
        else:
            self.freq[number] = 1
            if 1 not in self.freqSet:
                self.freqSet[1] = set()
            self.freqSet[1].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            old_freq = self.freq[number]
            if self.freq[number] > 1:
                self.freq[number] -= 1
                self.freqSet[old_freq].remove(number)
                if self.freq[number] not in self.freqSet:
                    self.freqSet[self.freq[number]] = set()
                self.freqSet[self.freq[number]].add(number)
            else:
                del self.freq[number]
                self.freqSet[old_freq].remove(number)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqSet and len(self.freqSet[frequency]) > 0