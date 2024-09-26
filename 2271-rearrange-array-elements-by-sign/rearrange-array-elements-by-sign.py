class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # nums consists of equal number of positive and negative integers.
        answer = []
        positive = []
        negative = []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        for pos,neg in zip(positive,negative):
            answer.append(pos)
            answer.append(neg)
        return answer

                
        