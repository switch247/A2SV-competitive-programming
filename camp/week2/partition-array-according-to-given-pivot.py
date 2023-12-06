class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        piv = []
        greater = []
        
        answer = []
        for i in nums:
            if i == pivot:
                piv.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                lesser.append(i)
        return lesser + piv + greater



        