class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = {}
        def dp(i):
            if i>=n:
                return 0
            if i not in cache:
                cache[i] = max(dp(i+1+ questions[i][1]) + questions[i][0], dp(i+1))
            return cache[i] 

        return dp(0)