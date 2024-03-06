class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1                 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        first = index
        
        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid 
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        last = index

        return [first, last]