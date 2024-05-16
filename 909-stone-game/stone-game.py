class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(start, end, flag, tot):
            if start>end or start>=len(piles):
                return tot > 0
            
            if flag:
                # alice
                return dp(start+1, end, not flag, tot+piles[start]) or  dp(start, end-1,not flag, tot+piles[end] )
            else:
                # Bob
                return   dp(start+1, end,not flag, tot-piles[start] ) or   dp(start, end-1, not flag,tot-piles[end])
            
        return dp(0,len(piles)-1, True, 0) 
