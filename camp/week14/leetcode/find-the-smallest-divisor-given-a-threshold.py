class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def pos(divisor):
            s = 0
            for num in nums:
                s += ceil(num/divisor)
                if s > threshold:
                    return False
            # print(s)
            return s <=threshold
        
        left , right = 1,max(nums)
        while left <= right:
            mid = (left + right)//2
            if pos(mid):
                right = mid - 1
            else:
                left = mid +1
        return left
        