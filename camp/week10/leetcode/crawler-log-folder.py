class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for log in logs:
            if log == "../":
                if len(s) != 0:
                    s.pop()
            elif log != "./":
                s.append(log)

        return len(s)
        