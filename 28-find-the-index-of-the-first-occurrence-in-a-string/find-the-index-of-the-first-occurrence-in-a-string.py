class Solution:
    def KMP_part_one(self,p : str) -> list:
        x = len(p)
        lps  = [0]*x
        i = 0 
        j = 1
        while j <x:
            if p[j] == p[i]:
                lps[j] = i+1
                i+=1
                j+=1
            else:
                if i==0:
                    lps[j] = 0
                    j+=1
                else:
                    i = lps[i-1]
        return lps
    def strStr(self, haystack: str, needle: str) -> int:
        LPS = self.KMP_part_one(needle)
        print(LPS)
        l, r = 0,0
        while r < len(haystack):
            if needle[l] == haystack[r]:
                l+=1
                r+=1
            else:
                if l==0:
                    r+=1
                else:
                    l = LPS[l - 1]
            if l >= len(needle):
                return r - len(needle)

        return -1
        
            
            
        

        # def pollfirst(hash, newchar,ln):
        #     base = 27
        #     mod = (10**9 )+7
        #     return (hash  - (ord(newchar)-96)* pow(base,ln)) %mod
        # def addlast(hash, newchar, leng):
        #     base = 27
        #     mod = (10**9 )+7
        #     return (hash * base + (ord(newchar)-96)) %mod
        

