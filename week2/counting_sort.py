def countingSort(arr):
    # Write your code here
    k = [0]*100
    t=""
    for i in arr:
        k[i] = k[i]+1
    for i in range(len(k)):
        if k[i]!=0:
            t +=((str(i)+" ")*k[i])
    return t.strip().split(" ")
#convert to string to make life easier
