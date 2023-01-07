class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.reverse()
        # nums[:k].reverse()
        # nums[k:].reverse()
        
        k=k%len(nums)  # doesn't work with out (this index out of range) 
        
       """
       k=4
       len(nums)= 9
       4%9 =4
       k=10
       len(nums)= 7
       10 % 7 = 3 it is not guarenteed that k is greater than lenght
       
       """
        
        
        
        n= len(nums)-1
        def rev(x,l,r):
            while(l<r):
                x[l],x[r] = x[r],x[l]
                l+=1
                r-=1
        
        rev(nums , 0 ,n)
        rev(nums , 0 ,k-1)
        rev(nums , k , n)
        
        
        
        # swallowed = [i:i+k]
        # for i in range (len(nums),k):
        #     swallowed = [i:i+k]
            
