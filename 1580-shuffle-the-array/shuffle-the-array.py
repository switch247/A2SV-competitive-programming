class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        left=0
        for i in range(n,2*n):
            ans.append(nums[left])
            left+=1
            ans.append(nums[i])
        return ans