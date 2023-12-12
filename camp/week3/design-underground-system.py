# from collections import defaultDict
class UndergroundSystem:

    def __init__(self):
        self.checkIn_dict = defaultdict(lambda:[])
        # self.checkOut_dict = defaultDict(lambda:[])
        self.average_dict = defaultdict(lambda:[])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # checkin {}= (id,station):time
        self.checkIn_dict[id]  = (stationName,t)
        # print(self.checkIn_dict.items())
        # id, entering time

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #sometimes exitors log might not be there ignore them
        # find where they entered 
        if id in self.checkIn_dict:
            enter_station, enter_time = self.checkIn_dict[ id ]
            time = t - enter_time
            self.average_dict[stationName] = self.average_dict[(enter_station, stationName)].append(time)
            # print(self.average_dict,"average")


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.average_dict[(startStation, endStation)]
        if not t:
            return 0
        n = len(t)
        average = sum (t)/ n
        return average
        
        

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
