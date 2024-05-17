class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        if m == 1 or n == 1: return A[0][0]
        
        _big = float('inf')

        dp = [[_big] * n for _ in range(m)]

        ans = _big

        def helper(row, col):
            if dp[row][col] != _big: return dp[row][col]

            if row == m - 1:  return A[row][col]

            left = right = _big

            if col > 0:
                left = helper( row + 1, col - 1)

            straight = helper( row + 1, col )

            if col < n - 1:
                right = helper( row + 1, col + 1 )
            # cur + min next
            dp[row][col] = min(left, min(straight, right)) + A[row][col]

            return dp[row][col]


        for i in range(len(A)):
            ans = min(ans, helper( 0, i))

        return ans

