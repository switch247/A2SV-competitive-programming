class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        #coount dictionary
        #check if number and its double exist
        #len(changed)%2!=0 list has to be even
        if len(changed)%2!=0:
            return []
        else:
            ans=[]

            changed.sort()
            c = Counter(changed) 
            for num in changed:
                if num ==0 and c[num]>=2:
                    c[num]-=2
                    ans.append(num)
                elif num>0 and (c[num] and c[2*num] ):#this doesnt work for 0 b/c 0*2 =0
                    c[num]-=1
                    c[num*2]-=1
                    ans.append(num)
            return ans if len(ans)==len(changed)//2 else []
        