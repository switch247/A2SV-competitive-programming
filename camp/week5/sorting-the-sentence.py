class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        d = []
        for word in arr:
            d.append((int(word[-1]), word[:-1]))
        print(d)
        return ' '.join([ x[1] for x in sorted(d) ])
        