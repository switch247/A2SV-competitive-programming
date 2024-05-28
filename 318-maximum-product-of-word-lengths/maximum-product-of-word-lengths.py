class Solution:
    def maxProduct(self, words: List[str]) -> int:
        x = [0]*26
        n =len(words)
        ans  =0
        def share(x,y):
            # print(x,y)
            z =  set(x) & set(y)
            # print(z)
            return len(z) !=0
        
        for i in range(n):
            for j in range(i+1,n):
                if not share( words[i],words[j] ):
                    # print(words[i],words[j])
                    ii, jj  = len(words[i]), len(words[j])
                    ans = max(ans,   ii*jj)

        return ans