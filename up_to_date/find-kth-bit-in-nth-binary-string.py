class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cache = {} #n:"str"
        def invert(s):
            str1 = ""
            for i in s:
                if i == "0":
                    str1 += "1"
                else:
                    str1 += "0"   
            return str1[::-1]
        def get(n):
            if n == 0: return "0"
            if (n) in cache: 
                return cache[(n)] + "1" + invert(cache[(n)]) 
            cache[(n)] = get(n-1)
            left = cache[n]
            right = invert(left)# o->1 and reverse
            return left + "1" + right
        return get(n)[k-1]
