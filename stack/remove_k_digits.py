class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #add value to stalk if stalk[-1]>i pop; then add to stalk
        stalk=[]
        for i in (num):
            while stalk and k>0 and int(stalk[-1]) > int(i):
                k-=1
                stalk.pop()   
            stalk.append(i)
        stalk=stalk[:len(stalk)-k] 
        # if there are elements that were not poped remove the lest k elements 
        ans=''.join(stalk)
        #if stalk is empty return '0'
        return str(int(ans)) if stalk else '0'
                    
#this was hard(if it wasnt catagorized in stalk i wouldnt have got it)
            
