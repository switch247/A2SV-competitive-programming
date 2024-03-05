class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d  = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        combinations = []
        if not digits:
            return []
        def backtrack(i, sub):
            # print(combinations)
            if i==len(digits):
                if len(sub)==len(digits):
                    combinations.append( ''.join(sub) )
                return
            for j in range(i,len(digits)):
                for ch in d[digits[j]]:
                    sub.append(ch)
                    backtrack(j+1, sub)
                    sub.pop()
        backtrack(0, [])
        return combinations