class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer=''
        if len(s)<=1 or k <= 1:
            answer+=s
            return answer
        else:
            for i in range(0, len(s),2*k):
                # increment by 2k
                first_k= s[i:i+k]
                # rev the first k chars
                rev_first_k = first_k[::-1]
                answer += (rev_first_k + s[i+k:i+2*k])
            return answer
        