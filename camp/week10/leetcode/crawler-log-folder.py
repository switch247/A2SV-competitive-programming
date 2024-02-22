class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for log in logs:
            if log !='./':
                if log=='../':
                    if s:
                        s.pop()
                else:
                    s.append(log)
        return len(s)
        