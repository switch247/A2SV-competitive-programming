class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        start = 1
        ops=0
        if maxDoubles==0: return target-1
        while target > 0:
            if maxDoubles ==0:
                return ops + target-1
                
            if target % 2 :
                target -= 1
            else:
                if maxDoubles > 0:
                    target = target//2
                    maxDoubles -= 1
                else:
                    target-=1
            # print(target)
            if target==0:
                break
            ops+=1
       
        return ops 
