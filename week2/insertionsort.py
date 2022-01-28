a = [1,4,8,6,3,7]
for i in range(1,len(a)):
    val = a[i]
    #if value to the lleft greater than current one switch
    while a[i-1] > a[i] and i>0:
        a[i-1], a[i] = a[i], a[i-1]
        i -= 1
        #b/c i-1 can go tp -ve index (i>0)
print(a)        
# pointer at index one and shift left and compare each adjesent value
