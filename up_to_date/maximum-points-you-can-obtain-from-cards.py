class Solution:#cnt be done recurcively because time limit excede
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #change to prefix sum form
        for i in range(1,len(cardPoints) ):#beter than sum(cardpoints[i:i+window])
            cardPoints[i] += cardPoints[i-1]
        tot = cardPoints[-1]
        if k == len(cardPoints): return tot
               
        window = len(cardPoints) - k
        print(cardPoints)
        min_sum= cardPoints[window-1] 
        # print(min_sum)
        for i in range(1, len(cardPoints)-window+1):
            # print(cardPoints[i+window-1] -cardPoints[i-1])
            min_sum= min(min_sum, cardPoints[i+window-1] -cardPoints[i-1]  )
            #max score= total sum - minsubstring sum 
        return cardPoints[-1] - min_sum
