class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      """
      move the right pointer if you incounter 1s
      move the right pointer and decrese flips left  if you incounter 0s
      move left pointer when you run out of flips
      """
        n =len(nums)
        left = 0
        for right in range(n):
            if nums[right] == 0:
                k-=1
            if k < 0:
                if nums[left] == 0:#regain the flip you used
                    k+=1               
                left += 1

        return right - left + 1
            



            
