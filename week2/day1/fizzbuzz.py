
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a=[];
    
        for n in range(1,n+1):
            if (n%3==0 and n%5==0):
                n = ("FizzBuzz")
                a.append(n)
            elif (n%5==0):
                n= ("Buzz")
                a.append(n)
            elif (n%3==0):
                n= ("Fizz")
                a.append(n)
            else:
                n=str(n)
                a.append(n)
            
        return a;
