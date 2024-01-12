class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        first_idx = {}
        # rep = set()
        ans = float('inf')
        for right in range( len(cards) ):
            if cards[right] in first_idx:
                # rep.add( f"{right}:{cards[right]}" )
                ans = min(ans, right - first_idx[cards[right]] + 1 )

            first_idx[ cards[right] ] = right
            
        # print(first_idx, rep)
        return ans if ans!=float('inf') else -1