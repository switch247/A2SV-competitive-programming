class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append( [ timestamp , value ] )
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.dict.get(key, [])
        # bisect_left
        l  , r = 0, len(vals)-1
        ans =''
        while l<=r:
            mid = (l+r)//2
            if vals[mid][0] <= timestamp:
                ans = vals[mid][1]
                l = mid +1
            else:
                r = mid -1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)