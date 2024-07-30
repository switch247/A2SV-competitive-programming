class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            temp = mx
            if arr[i] > mx:
                mx = arr[i]
            arr[i]  = temp
        arr[-1] = -1
        return arr
