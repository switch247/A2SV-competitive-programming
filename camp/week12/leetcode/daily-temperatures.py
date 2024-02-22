class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temp)
        for i, v in enumerate(temp):
            while stack and temp[stack[-1] ]< v:
                indexold = stack.pop()
                ans[indexold] = (i - indexold) # time until next high temp
            stack.append(i)
        return ans
        
                
            