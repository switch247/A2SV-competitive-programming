a = [1,4,8,6,3,7]
for i in range(len(a)-1):#switches current element with minimum from innner loop, last ele is considered sorted, leftside from i is sorted
    min = i
    for j in range(i+1,len(a)):#finds minimum ele starting from i to end
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]
print(*a)
