class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        for i in range(1,len(cardPoints) ):
            cardPoints[i] += cardPoints[i-1]
        tot = cardPoints[-1]
        if k == len(cardPoints): return tot
        #max score= tot- minsubstring        
        window = len(cardPoints) - k
        print(cardPoints)
        min_sum= cardPoints[window-1] 
        # print(min_sum)
        for i in range(1, len(cardPoints)-window+1):
            # print(cardPoints[i+window-1] -cardPoints[i-1])
            min_sum= min(min_sum, cardPoints[i+window-1] -cardPoints[i-1]  )
            
        return cardPoints[-1] - min_sum