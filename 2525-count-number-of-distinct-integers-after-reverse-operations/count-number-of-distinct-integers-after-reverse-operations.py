class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num=nums[:]
        #reverse all the elements in nums and store it in the num list
        for x in nums:
            sum=0
            while x>0:
                digit=x%10
                sum=sum*10+digit
                x=x//10
            num.append(sum)

        return len(list(set(num)))