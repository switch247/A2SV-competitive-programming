class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l=0
        s =[]
        for i in range(len(pushed)):
            s.append(pushed[i])
            while s and  popped[l] == s[-1]:
                s.pop()
                l+=1
                           
        return True if not s else False
