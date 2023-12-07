class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ''
        x = 0
        m  = len(spaces)
        for i,v in enumerate(s):
            if x < m and  i == spaces[x]:
                x += 1
                answer+= ' '
            answer += v
        return answer
            
        