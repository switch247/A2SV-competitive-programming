class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =[]+ nums
        self.prefix= self.nums[:]
        self.prefix.insert(0,0)
        # print(self.prefix)
        for i in range(1, len(self.prefix)):
            self.prefix[i] =   self.prefix[i] +  self.prefix[i-1]
        # print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
   
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)