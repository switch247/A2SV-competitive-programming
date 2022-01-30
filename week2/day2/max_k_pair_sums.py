class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a=0
        nums.sort() #sorting takes most of the time the rest is efficient
        l=0
        r = len(nums)-1
        while(l < r):
            if nums[l]+nums[r]==k:
                a+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
        return a
  '''#uses more time and space
  class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
         ans=0
         hash={}
        
         for x in nums:
                if k-x in hash:
                    ans+=1
                    if hash[k-x]==1:
                        del hash[k-x]
                    else:
                        hash[k-x]-=1
                else:
                    if x not in hash:
                        hash[x]=0
                    hash[x]+=1
         return ans
  '''
