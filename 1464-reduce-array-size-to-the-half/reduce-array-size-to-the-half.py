class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq =Counter(arr)
        
        size = len(arr)
        target = len(arr)//2
        answer=0
        heap_name = []
        for i in freq.values():
            heappush(heap_name,-i)

        while size > target:
            size +=  heappop(heap_name) 
            answer+= 1
            
        return answer