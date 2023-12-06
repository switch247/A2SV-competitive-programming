class Solution:
    def totalMoney(self, n: int) -> int:
        # monday%7 +1
        answer = monday = 0
        prev   = 1
        for i in range(n):
            if i%7 == 0:
                monday +=1
                answer += monday
                prev = monday
            else:
                prev += 1
                answer += prev 
        return answer

        