class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr2)

        idx = dict()

        for i,x in enumerate(arr2):
            if x not in idx :
                idx[x] = i
        
        left = [i for i in arr1 if count[i]] 
       
        right =  [j for j in arr1 if not count[j]]

        left.sort(key = lambda x : idx[x])
        right.sort()
        return left + right