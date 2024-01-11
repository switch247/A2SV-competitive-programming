class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # v=['a', 'e', 'i', 'o',  'u']
        mp = Counter()
        i = res = 0

        for j, ch in enumerate(s):
            mp[ch] += 1

            if j - i + 1 == k:
                res = max(res, sum(val for key, val in mp.items() if key in "aeiou"))
                mp[s[i]] -= 1
                if not mp[s[i]]:
                    mp.pop(s[i])
                
                i += 1
        
        return res

             