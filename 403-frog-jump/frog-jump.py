class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        @cache
        def dp(i, k):
            if i==n-1: return True
            if i>=n: return False
            if k<1: return False
            cur = stones[i]
            mn = False
            if i!=0:
                for j in range(i,n):
                    if stones[j] -cur == (k-1):
                        mn = dp(j,k-1)  
                        break
            same = False
            for j in range(i,n):
                if stones[j] - cur == (k):
                    same = dp(j,k)  
                    break
            pl = False
            if i!=0:
                for j in range(i,n):
                    if stones[j] -cur == (k+1):
                        pl = dp(j,k+1)  
                        break

            return pl or mn or same
        return dp(0,1)