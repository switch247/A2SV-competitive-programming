class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #  a+b > c, a+c > b, and b+c > a , where a, b ,c are length of sides of a triangle
        nums.sort(reverse = True)
        # print(nums)
        for i in range(len(nums)-2):
            if nums[i] < (nums[i+1] + nums[i+2]): #b+c > a a being the largest one of the 3
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

        