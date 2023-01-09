class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = end = head #mid moves once end twice slow+=1 fast+=2
        #end moves twice as fast as mid
        while end and end.next:
            mid = mid.next
            end = end.next.next
        return mid
