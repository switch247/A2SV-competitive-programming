class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort() #we sant power to be large at any given moment
        #if power >= tokens[i]: power-=tokens[i] score+=1
        # if score>0: power+=tokens[i] score-=1
        score,out= 0,0
        l , r = 0, len(tokens)-1
        while(l<=r):
            if (power>=tokens[l]):
                power-= tokens[l]
                score+=1
                l+=1
            elif(score>0 and l!=r):
                power+=tokens[r]
                score-=1
                r-=1
            else:#avoid time limit exceded
                break
            out = max(score,out)
        #print(power)    
        return out
