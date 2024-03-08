class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius=0
        for i in range(len(houses)): 
            left, right = 0, len(heaters)-1
            ans = float('inf')
            while left <= right:
                mid = (left + right)//2

                # find min radius for house i
                ans = min(ans, abs(heaters[mid] - houses[i]))

                if heaters[mid] > houses[i]:
                    right = mid -1
                else:
                    left = mid + 1
                
            radius= max(radius, ans)

        return radius