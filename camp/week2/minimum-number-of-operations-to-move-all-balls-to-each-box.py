class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        for i in  range( len(boxes) ):
            for j in range( len(boxes) ):
                answer[i] += abs(j - i)  *  int(boxes[j])
        return answer
        