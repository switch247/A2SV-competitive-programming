class Solution:
    def sortSentence(self, s: str) -> str:
        b=s.split()
        d={}
        for i in b:
            d[int(i[-1])]=i[0:-1]
        answer = []
        for i in  range(len(b)):
            answer.append ( d[i+1] )
            
        return ' '.join(answer)
        
