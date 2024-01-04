class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        ans = float('inf')
        # 1 2  2 1 -1 3 3 -1 
        # find min i+k+k -t
        out = None
        for i in range( len(nums) ):
            j , k = i+1, len(nums)-1
            while j < k :
                s = nums[i] + nums[j] + nums[k] 
                # print(nums[i] , nums[j] , nums[k] )
                if  abs(s - target) < ans: #1 min
                    # closness to target = abs(s - target)
                    ans = min(ans, abs(s - target) )
                    out = s
                # print(ans)
                if  s == target: #
                    j+=1
                    k-=1
                elif s < target :
                    j+=1
                else:
                    k-=1
        return out