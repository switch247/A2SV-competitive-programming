class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [''] * len(s)
        for ch,index in zip(s,indices):
            answer[index] = ch
        return ''.join(answer)
