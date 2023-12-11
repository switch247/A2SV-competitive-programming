class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        d={}
        for i,v in enumerate(arr):
            d[v] = d.get(v,0) +1
            if d[v]/n >0.25:
                return v

