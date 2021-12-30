#Output: [1,3,12,0,0]
#buble 9min
#nums=list(map(int,input().split()))
nums = [0,1,0,3,12]
for j in range (len(nums)):
    for i in range(len(nums)-1):
        if nums[i]==0:
            nums[i],nums[i+1] = nums[i],nums[i+1]
            nums[i],nums[i+1] = nums[i+1],nums[i]
    
print(nums)
