class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {"X--":-1, "--X":-1, "X++":1, "++X":1}
        ans = 0
        for x in operations:
            # print(x)
            ans += ops[x]
        return ans
        