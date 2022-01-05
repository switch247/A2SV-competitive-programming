class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    new.append(arr1[j])
        neww=[]
        for j in range(len(arr1)):#this needs to be sorted
            if arr1[j] not in arr2:
                neww.append(arr1[j])    
        neww.sort()            
        new+=neww    
        return new
      #this is super slow but uses litle space 
      #fix later
