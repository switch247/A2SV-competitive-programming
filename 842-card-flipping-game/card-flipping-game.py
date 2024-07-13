class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = set()
        n = len(fronts)
        for i in range(n): #o(n)
            if (fronts[i] == backs[i]):
                bad.add(fronts[i])
        # print(bad)
        # exclude cards which have the same back and front
        # because flipping these wont change anything but the rest are  good cards
        # and find the minimum of the rest
        mn = float('inf')
        for top, bottom in zip(fronts,backs): #o(n)
            if ( not bottom in bad ):
                mn = min( mn, bottom )
            if ( not top in bad ):
                mn = min( mn, top )            


        return   0 if mn == float('inf') else mn

    # min (in bottom not in up)