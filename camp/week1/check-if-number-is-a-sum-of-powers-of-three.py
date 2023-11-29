class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # x such that y == 3x.
        # 10  1 => 2 
        # 100 2 =>  3
        # print( log(10**7,3) )
        # print( log(n,3) == int(log(9,3))  )
        # print(sqrt(5,3),  )
        x = []
        for i in range( int(log(n,3))+1 ):
            x.append( 3**i )
        num = n
        sum = 0
        for i in range( len(x)-1 ,-1,-1):
            if sum + x[i] <= num :
                sum+= x[i]
            
        # print(sum)

        return sum == n
#  10 (10-1 = > 9)
#  1 (1-3 = >
        