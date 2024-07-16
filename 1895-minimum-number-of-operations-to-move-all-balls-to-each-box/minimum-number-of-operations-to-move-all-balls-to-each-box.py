class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        lcount,lcost,rcount,rcost = 0,0,0,0
        arr = [0]*n
        for i in range(1,n):
            if boxes[i-1] == '1':
                lcount+=1
            lcost += lcount
            arr[i] = lcost
        
        for i in range(n-2,-1,-1):
            if boxes[i+1] == '1':
                rcount +=1
            rcost+=rcount
            arr[i] += rcost
        return arr