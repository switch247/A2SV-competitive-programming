class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = list(zip(difficulty , profit))
        dp.sort()
        worker.sort()
        profit = 0
        start = 0
        mx = 0
        for skill in worker:
            while start < len(dp) and skill >= dp[start][0]:
                mx = max(mx, dp[start][1])
                start+=1
            # start = 0
            profit += mx
        return profit
        
