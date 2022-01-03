class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        #print(heights)
        #print(expected)
        count=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                #indices.add(heights[i])
                count+=1
        return count
