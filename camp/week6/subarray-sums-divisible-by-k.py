class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # runsum % k ==0
        ans = s = 0
        # sum: ocurence
        dic = {0:1} 
        for num in nums:
            s += num
            # print(s)
            if s % k in dic:
                ans += dic[s % k]     
            dic[ s % k ] = dic.get( s % k, 0 ) + 1
        # print(dic)
        return ans

   