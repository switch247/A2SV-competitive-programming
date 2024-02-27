class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ive 1/x^-n
        # odd x (x ^n//2) (x ^n//2)
        # even (x ^n//2) (x ^n//2)
        if n==0:
            return 1
        elif n==1:
            return x
        if n < 0:
            return  1 / self.myPow(x, abs(n) )
        val =   self.myPow(x, (n//2) ) 
        if n%2:
            return x * val * val
        else:
            return  val *val
        

            
        
