class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = 0
        c10 = 0
        for b in bills:
            if b == 10:
                c10 += 1
                if c5 < 1:
                    return False
                else:
                    c5 -= 1
            elif b == 20:
                if c5 >= 3 or (c5 >= 1 and c10 >= 1): #5 5 5 or 10 5
                    if c5 >= 1 and c10 >= 1:
                        c5 -= 1
                        c10 -= 1
                    elif c5 >= 3:
                        c5 -= 3
                else:
                    return False
            else:
                c5 += 1
        
        return True
       
            

        