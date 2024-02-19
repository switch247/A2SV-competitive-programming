class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        target_len = len(set(nums))
        d = {}
        l = r = 0
        ans = count = 0
        while r < n:
            # print(nums[r])
            d[nums[r]] = d.get(nums[r],0) + 1
            while len(d) == target_len :
                # print(  nums[l:r+1], nums[r+1:], n-r)
                # No of complete subarrays = length of main array - remaining elements on the right side of current complete subarray.
                # even if we include the elements on the right side of the array we have found to be complete the length of the dictonary will not increase
                # in other words  No of complete subarrays = number of elements to the right of the complete subarray + 1(1 meaning the complete subarray itself) 
                ans += (n - r )
                d[nums[l]] = d.get( nums[l], 0) - 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l+=1
            r+=1
        return ans

                
            
            




        