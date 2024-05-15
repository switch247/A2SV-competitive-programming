class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        cache = {}
        def dp(i, flag, x):
            if i >= n or x==2:
                return 0
            
            if flag:
                # sell
                if (i, flag, x) not in cache:
                    cache[(i, flag, x)]= max( dp(i+1, not flag,x+1) + prices[i], dp(i+1, flag,x) )
            else:
                # buy
                if (i, flag, x) not in cache:
                    cache[(i, flag, x)] =  max( dp(i+1, not flag,x) - prices[i], dp(i+1, flag,x) )
            return cache[(i, flag, x)]
        return dp(0,False, 0)