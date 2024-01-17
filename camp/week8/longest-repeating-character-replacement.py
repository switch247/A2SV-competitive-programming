class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def valid(c):
            z = sorted(c.values())
            z.pop() # pop the max
            if sum(z)<=k :return True
            else: return False
        left = right =0
        ans = 0
        rep = defaultdict(lambda:0)
        for  right in range( len(s) ):
            rep[s[right]] += 1
            while not valid(rep):
                rep[s[left]] -=1
                if rep[s[left]] == 0: del rep[s[left]]
                left +=1
            ans = max(ans, right - left + 1)

        return ans