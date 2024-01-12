class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # consecutive BLACKS dumbass
        def eval(c):
            W, B = c['W'], c['B']
            if B==k:
                return 0
            elif B==0:
                return k
            else:
                return W
        c = defaultdict( lambda: 0 )
        # print(len(blocks))
        left = 0
        ans = len(blocks)
        # only W and B
        for right in range( len(blocks) ):
            c[blocks[right]]+=1
            # print(right, blocks[right])
            if right- left + 1 == k:
                # print(c)
                ans = min( ans, eval(c) )
                c[blocks[left]]-=1
                left+=1

        return ans

