class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def o(n): return ord(n) -97
        def rev (o): return chr((o% 26 +97))
        z = list(map(o ,s))
        # print(z)
        x = [0] * (len(s) + 1)
        for a, b, c in shifts:
            if c == 0:
                x[a] -= 1
                x[b+1] += 1
            else:
                x[a] += 1
                x[b+1] -= 1

        
        for i in range (1, len(s)): x[i] += x[i-1]
            
        for i in range(len(s)):z[i] += x[i]
        # print(z, x, (0-1)%26)
        return ''.join(list(map(rev, z)))

        