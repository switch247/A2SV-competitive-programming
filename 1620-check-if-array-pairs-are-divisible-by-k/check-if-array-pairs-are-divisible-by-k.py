class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # (a + x)%k = 0
        #  x%k = (-a)%k
        if len(arr) % 2 == 1: return False
        d = defaultdict(lambda: 0)
        for num in arr:
            d[(num % k)] +=1
        
        if d[0]%2!=0:
            return False
        for num in arr:
            if d[ (-num) % k] != d[(num % k)]:
                return False
        return True

        """
        ● (a + b) % m = (a%m + b%m) % m
        ● (a - b) % m = (a%m - b%m) % m
        ● (a*b)%m = (a%m * b%m) % m
        ● If  (a - b) % m = 0, then  a%m = b%m
        """
        # n + 2rootn +1
        # isprime?
        # d = 2
        # while d*d<=d:
        #   if x%d==2: ret False
        #   d+1
        # ret True 
