#the hacker rank version is so dumb ;why not use actual insertion sort 
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
'''
def insertionSort1(n, arr):
    # Write your code here
    swallowed = arr[-1]
    
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > swallowed:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = swallowed
            print(*arr)
            break
    if arr[0] > swallowed:
        arr[0] = swallowed
        print(*arr)

'''
