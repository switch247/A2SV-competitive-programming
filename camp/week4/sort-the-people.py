class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # selection or insertion 
        # for i in range( len(names) - 1 ):
        #     mni = i
        #     for j in range( i+1 , len(names)):
        #         # print(heights[i], heights[j])
        #         if heights[mni] < heights[j]:
        #             mni = j
        #             heights[i], heights[mni] = heights[mni], heights[i]
        #             names[i], names[mni] = names[mni], names[i]
        # return names
        return [ z[0] for z in sorted(list(zip(names, heights)), key=lambda x :x[1], reverse=True) ]

