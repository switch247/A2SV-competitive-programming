class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        one = s.count('1')
        zero = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero+=1
            else:
                one-=1
            score = max(score,(one+zero) )
        return score
            

        