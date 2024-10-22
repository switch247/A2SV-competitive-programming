class Power:
    def myPow(self, x: float, n: int, mod : int = 1) -> float:
        # ive 1/x^-n
        # odd x (x ^n//2) (x ^n//2)
        # even (x ^n//2) (x ^n//2)
        if n==0:
            return 1
        elif n==1:
            return x
        if n < 0:
            return  1 / self.myPow(x, abs(n),mod ) 
        val =   self.myPow(x, (n//2), mod ) 
        if n%2:
            return( x * val * val) % mod
        else:
            return  (val *val) % mod
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        p = Power() 
        mod = 10**9 + 7
        if n%2:
            primes = n // 2
            evens = (n+1) // 2
        else:
            primes = n// 2
            evens = n // 2 
        
        # print('primes:', primes, 'evens:', evens)
        if primes > 0:
            return  ( p.myPow(4,primes,mod) * p.myPow(5,evens,mod) )% mod
        else:
            return   p.myPow( 5, evens,mod ) % mod


        # 1 # 0 - 9
        # 2 # 01 02 03 11 12 13 14 25 37 
        # 2 # 00-99
        # 11 
        # 123
        # ceil(n/2)
        # return 0
        # 5 4 5 4