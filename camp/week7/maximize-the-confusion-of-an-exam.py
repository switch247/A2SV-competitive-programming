class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        ans = 0
        for x in "TF":
            left ,  right = 0 , 0
            tolerance = k
            # consecutive t's or f's
            while right < n:
                if answerKey[right] !=x:
                    tolerance-=1
                while tolerance < 0:
                    ans = max(ans, right - left )
                    if answerKey[left] !=x:
                        tolerance+=1
                    left +=1
                right += 1
            ans = max(ans, right - left )
        return ans
