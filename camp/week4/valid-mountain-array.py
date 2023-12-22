class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        i, j = arr[0], arr[1]

        if i>= j:
            return False
        
        increasing = True
        for a , b in pairwise(arr):
            if a==b:
                return False
            if increasing:
                if a > b:
                    increasing = False
            else:
                if a < b:
                    return False
        return not increasing 

                


        