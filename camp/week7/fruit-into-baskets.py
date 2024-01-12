class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #find the largest consequtive substring with less than 3types of fruits
        ans = 0
        n = len(fruits)
        right=left=0
        x=defaultdict(lambda:0)
        for right,val in enumerate(fruits):
            x[val]+= 1
            while len(x) > 2:
                x[ fruits[left] ] -= 1
                if x[fruits[left] ] == 0:
                    del(x[ fruits[left] ])
                left +=1 
            ans= max(ans,right - left + 1)
            
        return ans
