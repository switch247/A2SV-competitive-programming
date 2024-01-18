class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # runsum == k -> runsum-k ==0
        ans = s = 0
        # sum: ocurence
        dic = {0:1} 

        for num in nums:
            s += num
            # print(s)
            if (s - k) in dic: ans += dic[s - k]     
            dic[s] = dic.get(s, 0) + 1
        # print(dic)
        return ans
    # -1 -1 1
    # -1 -2 -1 
    #  s - k 
    # using the prefix sum for each index check if there was a number we could subtract to get k 
    # num[i] - prevnumber == k 
    #  num[i] - k == prevnumber