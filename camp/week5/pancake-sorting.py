class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def swap_segments(arr, i, j):
            while i < j :
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1
        
        last = len(arr) -1
        ans = []
        while last > 0: 
            i = arr.index( max(arr[:last+1 ]) )
            # print(i, arr[i])
            if i ==last: # 0 operations
                # print('already at the end')
                pass
            elif i == 0: # 1 operation
                # print(i+1,".")
                ans.append( last+1 )
                swap_segments(arr, 0, last)
            else: # 2 operations
                # print(i+1,last,"..")
                ans.append(i+1)
                swap_segments(arr, 0, i)
                
                ans.append( last+1 )
                swap_segments(arr, 0, last)
            last-=1
            # print(arr)
        return ans

# 3 2 4 1 
# 4 2 3 1 a
# 1 3 2 4 a
# 3 1 2 4 b
# 2 1 3 4 b
# 1 2 3 4 c
        