class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        #coount dictionary
        #check if number and its double exist
        #len(changed)%2!=0 list has to be even
        if len(changed)%2!=0:
            return []
        else:
            ans=[]
            '''d={}
            for i in sorted(changed):
                if i in d:
                    d[i]+=1
                else:
                    d[i] == 1
                    '''
            changed.sort()
            c=Counter(changed) #same as above
            for i in changed:
                if i ==0 and c[i]>=2:
                    c[i]-=2
                    ans.append(i)
                elif i>0 and (c[i] and c[2*i] ):#this doesnt work for 0 b/c 0*2 =0
                    c[i]-=1
                    c[i*2]-=1
                    ans.append(i)
            return ans if len(ans)==len(changed)//2 else []
        
