class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x > arr[-1]:
            s = len(arr) -k 
            return arr[s:s+k]
        elif x <= arr[0]:
            return arr[:k]
        
        first = last = bisect_left(arr, x)
        # [1,1,1,10,10,10]
        while (last-first) <= k:
            if last>=len(arr) or (first>=0 and abs(arr[first]-x) <= abs(arr[last]-x)):
                first-=1
            else:
                last+=1
        # print(first,last)
        return arr[first+1:last]

        # return sorted(sorted(arr, key = lambda z : abs(x-z))[:k])