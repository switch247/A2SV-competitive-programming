class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_map = {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10,
                'k': 11,
                'l': 12,
                'm': 13,
                'n': 14,
                'o': 15,
                'p': 16,
                'q': 17,
                'r': 18,
                's': 19,
                't': 20,
                'u': 21,
                'v': 22,
                'w': 23,
                'x': 24,
                'y': 25,
                'z': 26
            }
        
        # c, b
        # b, a
        # a c d ,,c 
        # a c d , b 
        # a c d b, c

        count = Counter(s)
        # sset = set()
        stack = []
        for ch in s:
            # print(ch,end=' ')
            while stack and letter_map[stack[-1]] >= letter_map[ch] and count[stack[-1]] > 1 and ch not in stack:
                x = stack.pop()
                count[x]-=1 
            if ch not in stack:
                stack.append(ch)
            else:
                count[ch]-=1 
            # print(stack)
        return ''.join(stack)

        # pop stack decrease count 
        # strictictly increasing stack
        # dont pop in there is no duplicate element