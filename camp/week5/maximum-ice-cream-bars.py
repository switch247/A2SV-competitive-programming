class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        # print(costs)
        ans = 0
        for i in range(len(costs)):
            if costs[i] <= coins:
                coins -=costs[i]
                ans+=1
            else:
                break
        return ans
        