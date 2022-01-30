class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]] #add the 1st one before any thing
        for i , j in intervals[1:]:# [[i,j]]=[1,2] each element in each element
            l=answer[-1][1] # end value of last added interval to output
            if i <= l:
                answer[-1][1]=max(l,j)
            else:
                answer.append([i,j])
        return answer
    
