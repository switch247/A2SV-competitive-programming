class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}
        def dp(i, _sum):
            if _sum > amount:
                return  0
            if _sum==amount:
                return 1
            if i==-1:
                return 0
                
            if (i, _sum) not in cache:
                cache[(i, _sum)] =  dp( i, _sum+coins[i] ) +  dp(i-1, _sum) 
            return cache[(i, _sum)] 
        return dp(n-1, 0) 
        