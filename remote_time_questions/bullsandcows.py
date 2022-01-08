class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bul=0
        cow=0
        buk=[0]*10
        for s,g in zip(secret,guess):
            if s==g:
                bul+=1
            else:
                buk[int(s)]+=1
                buk[int(g)]-=1
        c=0
        for i in buk:
            if i > 0:
                c+=i
        cow =len(secret)-bul-c
      
        return ''.join([str(bul),'A',str(cow),'B'])
        
        
