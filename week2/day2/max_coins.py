class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)//3
        #len//3== steps taken by bob
        r=0
        left=0
        right=len(piles)-2
        for i in range(len(piles)-2,n-1,-2):
            r += piles[i]
        return r
        
        '''while left<right:
            r+=piles[right]
            left+=1
            right-=2
        return r'''
    
        
                     
        
                       
            

            
