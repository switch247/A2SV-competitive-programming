class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = (len(b)//len(a))
        for count in range(repeat + 3):
            if b in a*count:
                return count
        return -1