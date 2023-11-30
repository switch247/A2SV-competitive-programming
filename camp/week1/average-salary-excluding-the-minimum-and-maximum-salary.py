class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        return sum( sorted(salary)[1:-1] ) / (n-2)

        