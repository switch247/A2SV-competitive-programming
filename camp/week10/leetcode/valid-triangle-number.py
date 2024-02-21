class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # valid traingele = larger side is < sum of the other sides
        # a, b, c a <= b <= c 
        # a+b > c === valid
        nums.sort()
        # print(nums)
        n = len(nums)
        ans =0
        
        r = 2
        for k in range(2,len(nums)):
            i = 0
            j = k-1
            # print(i,j,k)
            while i < j:
                # print( nums[i], nums[j], nums[k])
                if nums[i] + nums[j] > nums[k]:
                    # print("//", i,j,k)
                    ans += (j - i )
                    j -= 1 
                else:
                    i += 1

        return ans
        # 1 2 3 4
