class Solution:
    def integerBreak(self, n: int) -> int:
        choices = [i for i in range(1,n)]
        # print(choices)
        m = len(choices)
        cache = {}
        def dp(i, _sum, _mult):
            if _sum > n:
                return  0
            if _sum==n:
                return _mult
            if i==-1:
                return 0
                
            if (i, _sum,_mult) not in cache:
                cache[(i, _sum,_mult)] =  max(dp( i, _sum+choices[i], _mult*choices[i] ), dp(i-1, _sum, _mult) )
            return cache[(i, _sum,_mult)] 
        return dp(m-1, 0,1) 