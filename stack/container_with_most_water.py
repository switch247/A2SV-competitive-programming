class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)-1
        l =0
        width = r 
        #output = 0
        stalk=[]
        m=0
        stalk.append(min(height[l], height[r])*width)
        while (l < r):
            m= min(height[l], height[r])*width
            #output = max(output, min(height[l], height[r])*width)# i could do this using a stalk
            if height[l] < height[r]:
                l+=1          
                width-=1
            else:
                r-=1
                width-=1
            while stalk and stalk[-1] < m:
                #stalk.pop
                stalk.append(min(height[l], height[r])*width)
        #return output
        return stalk[-1];
    # (take the minimum of your left and right pointer) *width => add it to stalk
    # if left<right: leftpointer+=1,width-=1
    #if right < left: rightpointer-=1,width-=1
    # if stalk[-1]< the min of right*width,left*width :  add the new value
    
