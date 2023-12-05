class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # you have to pass in order
        time = 0
        prev = points[0]
        # print( (sqrt(2)*2 ) + 1 + sqrt(2)*4 )
        for i in range(1, len(points)):
            current = points[i]
            x1 = prev[0]
            y1 = prev[1]
            x2 = current[0]
            y2 = current[1]
            hor =  abs(  x2  -   x1  )
            ver =  abs( y2  -   y1  )
            # print(hor , ver)
            n  = max (  hor ,  ver   )
            time += n
            prev = current
        return time




            
