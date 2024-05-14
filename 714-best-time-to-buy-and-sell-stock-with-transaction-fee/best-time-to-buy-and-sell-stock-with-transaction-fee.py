class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cache = {}

        def dp(i,flag):
            if i >= n:
                return 0
            if flag:
                if (i,flag) not in cache:
                    cache[(i,flag)] = max(dp(i+1,not flag) +prices[i]-fee , dp(i+1,flag) )
            if not flag:
                if (i,flag) not in cache:
                    cache[(i,flag)] = max(dp(i+1,not flag) -prices[i] , dp(i+1,flag) )
            
            return cache[(i,flag)]
        
        return dp(0,False)