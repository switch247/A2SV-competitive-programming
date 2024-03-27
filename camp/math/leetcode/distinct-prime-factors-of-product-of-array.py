class Solution:
    def primefactorization(self ,n):
            if n < 2:
                return []
            x = []
            for i in range(2,n):
                while n%i == 0:
                    x.append(i)
                    n//=i
            if n>1:
                x.append(n)
            return x

    def isprime(self,num):
        if num < 2 :
            return False
        
        d =2
        while d*d<=num:
            if d*d==num:
                return False
        return False
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        for num in nums:
            for j in list(set(self.primefactorization(num))):
                primes.add(j)
        
        return len(primes)