class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        e = 0 
        d = {}
        answer = []
        for i,v in enumerate(nums):
            if v%2 ==0:
                d[i] = "even"
                e+=v
            else:
                d[i] = "odd"
        print(d)     
        for a,b in queries:
            # i = d[b]
            x = nums[b] + a
            if x%2 == 0:
                if d[b] =="odd":
                    e += x
                    d[b] = "even"
                else:
                    e += a
                    
            else:
                if d[b] == "even":
                    e -= nums[b]
                    d[b] = "odd"
                
            nums[b] = x
            answer.append(e)
        return answer 