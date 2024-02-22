class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        n = len(deck)
        queue = deque()
        # folllow the example bottom up
        for i in range(n):
            if queue:
                targ = queue.pop()
                queue.appendleft(targ)
            queue.appendleft(deck[i])
        return queue
        

        

