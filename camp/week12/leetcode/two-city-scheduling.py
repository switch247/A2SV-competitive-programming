class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        m= len(costs)
        n = m//2
        costs.sort(key = lambda x:(x[0] - x[1]) )
        # print(costs)
        l, r = 0, m-1
        ans = 0
        for i in range(m):
            if i < n:
                ans+= costs[i][0]
            else:
                ans+= costs[i][1]

            
        return ans