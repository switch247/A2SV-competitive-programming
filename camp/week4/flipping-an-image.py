class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        cpy = [row[::-1] for row in image]

        for i in range( len(image) ):
            for j in range( len(image[0]) ):
                if cpy[i][j] ==0:
                    cpy[i][j] = 1
                else:
                    cpy[i][j] = 0
        return cpy
        