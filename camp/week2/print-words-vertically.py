class Solution:
    def printVertically(self, s: str) -> List[str]:
        z = s.split()
        max_len = len(max(z, key=len))
        ans =  [ '' ]*max_len
        
        for i in range(len(z) ):
            cur_len = len(z[i])
            if cur_len < max_len:
                z[i] =  z[i] + " " * (max_len - cur_len) 
            for j in range(max_len):
                ans[j] += z[i][j]
        
        for i in range(len(ans)) :
            ans[i] = ans[i].rstrip()
            
        return ans
        