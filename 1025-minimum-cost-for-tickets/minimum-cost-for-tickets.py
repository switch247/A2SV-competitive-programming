class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = {}
        def dp(i):
            if i>=n:
                return 0
            if i not in cache:
                j = k = i+1
                while j<n and days[j]<days[i]+ 7:
                    j+=1
                while k<n and days[k]<days[i]+ 30:
                    k+=1
                _one = dp(i+1) + costs[0]
                _seven = dp(j) + costs[1]
                _thirty = dp(k) + costs[2]
                cache[i]  = min(_one,_seven, _thirty)
            return  cache[i] 
        return dp(0)