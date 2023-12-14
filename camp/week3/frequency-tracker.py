class FrequencyTracker:

    def __init__(self):
        self.freq_dict = {}
        self.dict_of_freqs = {}

    def add(self, number: int) -> None: 
        self.freq_dict[number] = self.freq_dict.get(number, 0 ) +1 

        self.dict_of_freqs[ self.freq_dict[number] ] = self.dict_of_freqs.get(self.freq_dict[number], 0) +1
        # decrease count of previous frequency
        self.dict_of_freqs[ self.freq_dict[number] -1 ] = self.dict_of_freqs.get(self.freq_dict[number] -1 , 1) -1

    def deleteOne(self, number: int) -> None:
        if number in self.freq_dict:
            self.dict_of_freqs[self.freq_dict[number]] = self.dict_of_freqs.get(self.freq_dict[number], 1) - 1
            if self.freq_dict[number] >1:
                self.freq_dict[number] = self.freq_dict.get(number, 0 ) - 1 

                self.dict_of_freqs[ self.freq_dict[number] ] = self.dict_of_freqs.get(self.freq_dict[number], 0) +1
            
            else:
                del(self.freq_dict[number])
            

    def hasFrequency(self, frequency: int) -> bool:
        # print( frequency, self.dict_of_freqs )
        if frequency in self.dict_of_freqs and self.dict_of_freqs[frequency] > 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)