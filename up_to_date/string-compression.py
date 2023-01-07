class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j=0,0
        s=[]
        n=len(chars)
        while( j<n ):
            while(j<n  and chars[i]==chars[j] ):
                j+=1
            s.append(chars[i])
            if j-i >1:
                for x in str(j-i):
                    s.append(x)
            i=j
            
        chars[:]= s
        return len(s)
