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