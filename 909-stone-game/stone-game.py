class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(start, end, flag):
            if start>end or start>=len(piles):
                return 0
            
            if flag:
                # alice
                return max(piles[start]+ dp(start+1, end, not flag), piles[end]+ dp(start, end-1,not flag))
            else:
                # Bob
                return  min( -piles[start]+ dp(start+1, end,not flag), -piles[end]+ dp(start, end-1, not flag))
            
        return dp(0,len(piles)-1, True)>0
