class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        reverse_winsize =  len(cardPoints) -  k
        tot  = sum(cardPoints)
        left = 0
        if reverse_winsize==0: return tot
        ans = float('inf')
        ss = 0
        for right in range( len(cardPoints) ):
            ss+=cardPoints[right]
            if right-left + 1 == reverse_winsize:
                ans = min (ans, ss )
                ss-=cardPoints[left]
                left+=1
        return tot - ans