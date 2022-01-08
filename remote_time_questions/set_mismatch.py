class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        r=[]
        #only one duped and replaced
        dup= sum(nums)- sum(set(nums))
        #r.append(dup)
        #list=1......n
        rep=sum(range(1,len(nums)+1)) - sum(set(nums))
        #dont forget len+1
        #r.append(rep)
        return [dup,rep]
                
                
                            
                          
                          
