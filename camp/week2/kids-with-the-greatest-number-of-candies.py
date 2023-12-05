class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCount = max(candies)
        
        # Output
        n = len(candies)
        
        # Since we can give each kid "extraCandies" amount of candies
        # If after giving each kid this amount, the total candies becomes >= maxCount
        # Then that means, we can set True for that kid
            
        return [candies[i] + extraCandies >= maxCount for i in range(n)]