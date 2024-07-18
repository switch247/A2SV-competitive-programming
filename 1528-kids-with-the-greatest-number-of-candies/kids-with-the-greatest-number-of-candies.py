class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        target = max(candies)
        answer = []
        for candy in candies:
            if candy + extraCandies >= target:
                answer.append(True)
            else:
                answer.append(False)
        return answer