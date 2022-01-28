a = [1,4,8,6,3,7]
for i in range(len(a)-1):#switches current element with minimum from innner loop, last ele is considered sorted, leftside from i is sorted
    min = i
    for j in range(i+1,len(a)):#finds minimum ele starting from i to end
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]
print(*a)


'''#using class and functions to be fancy(this didn't need to be complicated)
#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return min(arr[i:])
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            selected = self.select(arr, i)#gets minimum from select function
            selected_pos = arr[i:].index(selected) + i
            
            temp = arr[i]
            arr[i] = selected
            
            arr[selected_pos] = temp

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

'''
