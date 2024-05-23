class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def dp(i,j):
            ans  = float('inf')
            for k in range(i+1,j):
                cur = values[i]*values[j]*values[k]
                ans = min(ans, ( cur + dp(k,j) + dp(i,k) ) )

            return ans if ans!=float('inf') else 0
       
        return dp(0, len(values)-1)